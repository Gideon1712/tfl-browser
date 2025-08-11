terraform {
  required_version = ">= 1.5.0"
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
    }
  }
}

provider "azurerm" {
  features {}
  # We already exported ARM_* env vars from your service principal.
  # This tells the provider not to try slow auto-registration.
  skip_provider_registration = true
}
