
class CustomResponseCode(CustomCodeBase):

    HTTP_200 = (200, 'Success')
    HTTP_201 = (201, 'New Success Request')
    HTTP_202 = (202, 'The request processing has not yet been completed')
    HTTP_204 = (204, 'No content was returned')
    HTTP_400 = (400, 'Request error')
    HTTP_401 = (401, 'Unauthorized')
    HTTP_403 = (403, 'Access is prohibited')
    HTTP_404 = (404, 'The requested resource does not exist')
    HTTP_410 = (410, 'The requested resource has been permanently deleted')
    HTTP_422 = (422, 'Request parameter is illegal')
    HTTP_425 = (425, 'The server could not meet the requirements')
    HTTP_429 = (429, 'Too many requests, server restrictions')
    HTTP_500 = (500, 'Internal server error')
    HTTP_502 = (502, 'Gateway error')
    HTTP_503 = (503, 'The server is temporarily unable to process the request')
    HTTP_504 = (504, 'Gateway timeout')
