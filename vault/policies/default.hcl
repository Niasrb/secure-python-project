# Politique par défaut
path "secret/*" {
  capabilities = ["create", "read", "update", "delete", "list"]
}

# Politique pour l'API
path "secret/data/api/*" {
  capabilities = ["read", "list"]
}

# Politique pour les bases de données
path "secret/data/database/*" {
  capabilities = ["create", "read", "update", "delete", "list"]
}

# Politique pour l'audit
path "sys/audit/*" {
  capabilities = ["sudo", "read"]
}

# Politique pour la gestion des politiques
path "sys/policies/*" {
  capabilities = ["create", "read", "update", "delete", "list"]
}