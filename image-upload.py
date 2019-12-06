from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

#Upload Image using FORM DATA
class ImageView(APIView):
    """
    upload image using form data
    """
    def post(self,request):
        data = request.data['image']
        file_name = random.randint(00000,99999)
        path = default_storage.save('tempimage/'+str(file_name)+'.jpeg', ContentFile(data.read()))
        message = "http://" + str(get_current_site(request))+'/media/'+path
        return Response({"file_name":message})
