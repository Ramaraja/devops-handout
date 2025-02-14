provider "kubernetes" {
  config_path = "~/.kube/config"
}

resource "kubernetes_namespace" "test_namespace" {
  metadata {
    name = "test-namespace"
  }
}

resource "kubernetes_pod" "test_pod" {
  metadata {
    name      = "nginx-pod"
    namespace = kubernetes_namespace.test_namespace.metadata[0].name
  }

  spec {
    container {
      name  = "nginx"
      image = "nginx:latest"

      port {
        container_port = 80
      }
    }
  }
}

data "kubernetes_pod" "test_pod" {
  metadata {
    name      = kubernetes_pod.test_pod.metadata[0].name
    namespace = kubernetes_namespace.test_namespace.metadata[0].name
  }
}

output "pod_phase" {
  value = data.kubernetes_pod.test_pod.status
}