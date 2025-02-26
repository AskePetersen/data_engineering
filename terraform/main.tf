terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "6.22.0"
    }
  }
}

provider "google" {
  credentials = "./terraform keys/meta-plateau-452109-k1-7304406cdc98.json"
  project = "meta-plateau-452109-k1"
  region  = "us-central1"
}

resource "google_storage_bucket" "demo-bucket" {
  name          = "meta-plateau-452109-k1"
  location      = "US"
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}
