provider "google" {
  project = var.project_id
  region  = var.region
}

resource "google_container_cluster" "primary" {
  name     = "expense-cluster"
  location = var.region
  initial_node_count = 1
  remove_default_node_pool = true
}

resource "google_sql_database_instance" "db" {
  name             = "expense-db"
  region           = var.region
  database_version = "POSTGRES_13"

  settings {
    tier = "db-f1-micro"
  }
}
