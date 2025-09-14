terraform {
  backend "gcs" {
    bucket = "expense-tf-state"
    prefix = "terraform/state"
  }
}
