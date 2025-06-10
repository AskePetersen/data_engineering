variable "credentials" {
  description = "Credentials"
  default     = "./terraform keys/my-creds.json"
}

variable "project" {
  description = "project"
  default     = "meta-plateau-452109-k1"
}

variable "region" {
  description = "Region"
  default     = "europe-west3"
}

variable "location" {
  description = "Our location"
  default     = "EU"
}

variable "bq_dataset_name" {
  description = "My BigQuery Dataset Name"
  default     = "demo_dataset"
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  default     = "meta-plateau-452109-k1"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}
