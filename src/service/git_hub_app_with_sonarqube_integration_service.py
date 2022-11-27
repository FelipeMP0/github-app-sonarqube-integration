from generated import service_pb2_grpc as pb2_grpc
from generated import service_pb2 as pb2


class GitHubAppWithSonarQubeIntegrationService(
    pb2_grpc.GitHubAppWithSonarQubeIntegrationServicer
):
    def GetServerResponse(self, request, context):
        message = request.message
        result = {"message": message, "received": True}

        return pb2.MessageResponse(**result)
