variable "project_prefix" {
  description = "Short name prefix"
  type        = string
  default     = "tfl"
}

variable "location" {
  description = "Azure region"
  type        = string
  default     = "uksouth"
}

variable "node_count" {
  description = "AKS node count"
  type        = number
  default     = 1
}

variable "node_vm_size" {
  description = "AKS VM size"
  type        = string
  default     = "Standard_B2s"
}

variable "vnet_address_space" {
  description = "VNet CIDR"
  type        = string
  default     = "10.10.0.0/16"
}

variable "subnet_address_prefix" {
  description = "Subnet CIDR"
  type        = string
  default     = "10.10.1.0/24"
}

variable "kubernetes_version" {
  description = "Pin AKS k8s version (optional)"
  type        = string
  default     = ""
}
