import noisereduce as nr 
from scipy.io import wavfile
from django.shortcuts import render
import myprosody
from . import testpro
from os import path
import os
from pydub import AudioSegment
import base64
from datetime import date, datetime
def view_for_prosd(request):
    """
    Can access files from front-end form and validates them
    """
    if request.method == 'POST':
        body = request.body
        encoded = base64.b64decode(body)
        print("view pros")
        with open("myprosody//dataset//audioFiles//pzm12a.wav", "wb") as f:
            f.write(encoded)
        # src = "D:\\dj\\projects\\testprojects\\myprosody-master\\app\\myprosody\\dataset\\audioFiles\\pzm12a.wav"
        src = os.path.join("myprosody\\dataset\\audioFiles\\pzm12a.wav")
        dst = os.path.join("myprosody\\dataset\\audioFiles\\output.wav")
        # dst = "D:\\dj\\projects\\testprojects\\myprosody-master\\apipp\\myprosody\\dataset\\audioFiles\\output.wav"
#convert wav to mp3
        sound = AudioSegment.from_file(src)
        sound.export(dst, format="wav")
        print("done")
        rate, data = wavfile.read("D:\\dj\\projects\\testprojects\\myprosody-master\\app\\myprosody\\dataset\\audioFiles\\output.wav") 
        noisy_part = data[10000:15000] 
        reduced_noise = nr.reduce_noise(audio_clip=data,noise_clip=noisy_part, verbose=True) 
        # b=testpro.mysplev()
        
        a=testpro.mysptotal()
        print("Mysptotal is :---------------------------")
        print(a)

        
        return render(request, 'main.html',{'a':a})
    return render(request, 'main.html')
    


def out(request):
    if request.method == 'POST':
        a=testpro.mysptotal()
        print("Mysptotal is :---------------------------")
        print(a)
        
        b=testpro.myspgend()
        print("myspgend is :---------------------------")
        print(b)

        c=testpro.mysplev()
        print("mysplev is :------------------------------")
        print("c-->" ,c)
        


        d=testpro.mysppron()
        print("mysppron is :---------------------------")
        print("d = pron-->",d)
        # print(b,"value of b")


        e=testpro.myprosody()
        print("myprosody is  --------------------------")
        print("e = sody-->",e)


        return render(request, 'main.html',{'a':a,'b':b,'d':d,'e':e})
    return render(request, 'main.html')




# def out(request):
#     if request.method == 'POST':
#         a=testpro.mysptotal()
#         print("Mysptotal is :---------------------------")
#         print("com[*((^&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&77")


#         # import wavfile
#         # rate, data = wavfile.read("D:\\dj\\projects\\testprojects\\myprosody-master\\app\\myprosody\\dataset\\audioFiles\\output.wav") 
#         # noisy_part = data[10000:15000] 
#         # reduced_noise = nr.reduce_noise(audio_clip=data,noise_clip=noisy_part, verbose=True) 
#         # b=testpro.mysplev()
        
        
#         c=testpro.myspgend()
#         print("myspgend is :---------------------------")

#         print(c)
#         # print(b,"value of b")
#         return render(request, 'main.html',{'c':c,'a':a})
#     return render(request, 'main.html')




























# # import noisereduce as nr 
# # from scipy.io import wavfile
# from django.shortcuts import render
# import myprosody
# from . import testpro
# from os import path
# from pydub import AudioSegment
# import base64
# from datetime import date, datetime
# def view_for_prosd(request):
#     """
#     Can access files from front-end form and validates them
#     """
#     if request.method == 'POST':
#         body = request.body
#         encoded = base64.b64decode(body)
#         with open("myprosody//dataset//audioFiles//pzm12a.wav", "wb") as f:
#             f.write(encoded)
#         src = "D:\\dj\\projects\\testprojects\\myprosody-master\\app\\myprosody\\dataset\\audioFiles\\pzm12a.wav"
#         dst = "D:\\dj\\projects\\testprojects\\myprosody-master\\app\\myprosody\\dataset\\audioFiles\\output.wav"
# #convert wav to mp3
#         sound = AudioSegment.from_file(src)
#         sound.export(dst, format="wav")
#         print("done")
#         a=testpro.mysptotal()
#         print("Mysptotal is :---------------------------")
#         print(a)


#         # import wavfile
#         # rate, data = wavfile.read("D:\\dj\\projects\\testprojects\\myprosody-master\\app\\myprosody\\dataset\\audioFiles\\output.wav") 
#         # noisy_part = data[10000:15000] 
#         # reduced_noise = nr.reduce_noise(audio_clip=data,noise_clip=noisy_part, verbose=True) 
#         # b=testpro.mysplev()
        
        
#         c=testpro.myspgend()
#         print("myspgend is :---------------------------")

#         print(c)
#         # print(b,"value of b")
#         return render(request, 'main.html',{'c':c,'a':a})
#     return render(request, 'main.html')







