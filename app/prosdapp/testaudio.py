# # import librosa
# # # audio_data = 'D:\\dj\\projects\\testprojects\\myprosody-master\\app\\myprosody\\dataset\\audioFiles\\6b06b796bde05fda1a55f026c6dca89f.wav'
# # audio_data = 'D:\\dj\\projects\\testprojects\\myprosody-master\\app\\myprosody\\dataset\\audioFiles\\pzm12a.wav'
# # x , sr = librosa.load(audio_data)
# # print(type(x), type(sr))
# # print(x.shape, sr)

# from pydub import AudioSegment

# AudioSegment.from_wav("D:\\dj\\projects\\testprojects\\myprosody-master\\app\\myprosody\\dataset\\audioFiles\\pzm12a.wav").export("D:\\dj\\projects\\testprojects\\myprosody-master\\app\\myprosody\\dataset\\audioFiles\\pzm12a.mp3", format="mp3")



# from os import path
# from pydub import AudioSegment

# #files

# src = "D:\\dj\\projects\\testprojects\\myprosody-master\\app\\myprosody\\dataset\\audioFiles\\pzm12a.wav"
# dst = "D:\\dj\\projects\\testprojects\\myprosody-master\\app\\myprosody\\dataset\\audioFiles\\output.wav"

# #convert wav to mp3
# sound = AudioSegment.from_file(src)
# sound.export(dst, format="wav")
# print("done")





