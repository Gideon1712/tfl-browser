locals {
  rg_name     = "${var.project_prefix}-rg"
  vnet_name   = "${var.project_prefix}-vnet"
  subnet_name = "${var.project_prefix}-subnet"
  aks_name    = "${var.project_prefix}-aks"
  dns_prefix  = "${var.project_prefix}-dns"
  tags        = { project = var.project_prefix, env = "dev" }
}

# 1) Resource Group
resource "azurerm_resource_group" "rg" {
  name     = local.rg_name
  location = var.location
  tags     = local.tags
}

# 2) Networking: VNet + Subnet
resource "azurerm_virtual_network" "vnet" {
  name                = local.vnet_name
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  address_space       = [var.vnet_address_space]
  tags                = local.tags
}
resource "azurerm_subnet" "subnet" {
  name                 = local.subnet_name
  resource_group_name  = azurerm_resource_group.rg.name
  virtual_network_name = azurerm_virtual_network.vnet.name
  address_prefixes     = [var.subnet_address_prefix]
}

# 3) AKS (Managed Identity, Azure CNI Overlay networking)
resource "azurerm_kubernetes_cluster" "aks" {
  name                = local.aks_name
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  dns_prefix          = local.dns_prefix

  kubernetes_version = var.kubernetes_version != "" ? var.kubernetes_version : null

  default_node_pool {
    name                 = "system"
    vm_size              = var.node_vm_size
    node_count           = var.node_count
    vnet_subnet_id       = azurerm_subnet.subnet.id
    auto_scaling_enabled = false
  }

  identity { type = "SystemAssigned" }

  network_profile {
    network_plugin      = "azure"
    network_plugin_mode = "overlay" # IP-friendly, easy setup
    outbound_type       = "loadBalancer"
  }

  role_based_access_control_enabled = true
  oidc_issuer_enabled               = true
  workload_identity_enabled         = false

  tags = local.tags
}
