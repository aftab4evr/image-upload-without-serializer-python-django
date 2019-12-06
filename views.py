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

#Upload Image in base64
class Base64ImageView(APIView):
    """
    upload image using base64
    {
    "image":"bas6cod"
    }
    """
    def post(self,request):
        image = request.data['image']
        file_name = random.randint(00000,99999)
        with open("media/tempimage/"+str(file_name)+".png", "wb") as fh:
            fh.write(base64.decodebytes(image.encode()))
        message = "http://" + str(get_current_site(request))+'/media/tempimage/'+str(file_name)+".png"
        return Response({"file_name":message})
