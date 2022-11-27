from concurrent import futures
import grpc
from grpc_reflection.v1alpha import reflection
from generated import service_pb2_grpc as pb2_grpc
from generated import service_pb2 as pb2
from service import git_hub_app_with_sonarqube_integration_service as service


def serve():
    appService = service.GitHubAppWithSonarQubeIntegrationService()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_GitHubAppWithSonarQubeIntegrationServicer_to_server(appService, server)
    SERVICE_NAMES = (
        pb2.DESCRIPTOR.services_by_name["GitHubAppWithSonarQubeIntegration"].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
