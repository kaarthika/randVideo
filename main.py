
import random
from moviepy.editor import *
import moviepy
import moviepy.video.fx.all as vfx
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

#generate random numbers
intro_vid_int = random.randint(1, 3)
spying_int = random.randint(1, 3)
intro_int = random.randint(1, 6)
self_1_int = random.randint(1, 5)
self_2_int = random.randint(1, 5)
while self_1_int == self_2_int:
    self_2_int = random.randint(1, 5)
kaarthika_1_int = random.randint(1, 13)
kaarthika_2_int = random.randint(1, 13)
while kaarthika_1_int == kaarthika_2_int:
    kaarthika_2_int = random.randint(1, 13)
film_int = random.randint(1, 3)
breath_int = random.randint(1, 9)
om_int = random.randint(1, 8)
igstories_int = random.randint(1, 3)
water_int = random.randint(1, 4)
other_1_int = random.randint(1, 9)
other_2_int = random.randint(1, 9)
while other_1_int == other_2_int:
    other_2_int = random.randint(1, 9)
other_3_int = random.randint(1, 9)
while other_3_int == other_2_int or other_3_int == other_1_int:
    other_3_int = random.randint(1, 9)

#load video clips
print("video/water/3.mp4")
water = VideoFileClip("video/water/3.mp4")
water = water.rotate(90)
print("video/water/location/scotland.MOV")
scotland = VideoFileClip("video/water/location/scotland.MOV")
print("video/water/location/ny.MOV")
ny = VideoFileClip("video/water/location/ny.MOV")
print("video/water/location/houston.MOV")
houston = VideoFileClip("video/water/location/houston.MOV")
print("video/water/location/cville.MOV")
cville = VideoFileClip("video/water/location/cville.MOV")
print("video/water/location/sf.MOV")
sf = VideoFileClip("video/water/location/sf.MOV")
print("video/film/" + str(film_int) + ".mp4")
film = VideoFileClip("video/film/" + str(film_int) + ".mp4")
film = film.resize(tape.size)
print("video/igstories/"+str(igstories_int)+".mp4")
igstories = VideoFileClip("video/igstories/"+str(igstories_int)+".mp4")
print("video/intro/"+str(intro_vid_int)+".mp4")
intro_vid = VideoFileClip("video/intro/"+str(intro_vid_int)+".mp4")
print("video/tape.mp4")
tape = VideoFileClip("video/tape.mp4")
water = water.resize(tape.size)

#load audio clips
print("sound/intro/"+str(intro_int)+".mp3")
intro_sound = AudioFileClip("sound/intro/"+str(intro_int)+".mp3")
print("sound/breath/"+str(breath_int)+".mp3")
breath = AudioFileClip("sound/breath/"+str(breath_int)+".mp3")
print("sound/kaarthika/kaarthika"+str(kaarthika_1_int)+".mp3")
kaarthika_1 = AudioFileClip("sound/kaarthika/kaarthika"+str(kaarthika_1_int)+".mp3")
print("sound/kaarthika/kaarthika"+str(kaarthika_2_int)+".mp3")
kaarthika_2 = AudioFileClip("sound/kaarthika/kaarthika"+str(kaarthika_2_int)+".mp3")
print("sound/om/"+str(om_int)+".mp3")
om = AudioFileClip("sound/om/"+str(om_int)+".mp3")
print("sound/spying/"+str(spying_int)+".mp3")
spying = AudioFileClip("sound/spying/"+str(spying_int)+".mp3")

#load photos
print("still/other/"+str(other_1_int)+".jpg")
other_1 = ImageClip("still/other/"+str(other_1_int)+".jpg")
print("still/other/"+str(other_2_int)+".jpg")
other_2 = ImageClip("still/other/"+str(other_2_int)+".jpg")
print("still/other/"+str(other_3_int)+".jpg")
other_3 = ImageClip("still/other/"+str(other_3_int)+".jpg")
print("still/self/"+str(self_1_int)+".jpg")
self_1 = ImageClip("still/self/"+str(self_1_int)+".jpg")
print("still/self/"+str(self_2_int)+".jpg")
self_2 = ImageClip("still/self/"+str(self_2_int)+".jpg")

#get lengths
intro_sound_time = intro_sound.duration
om_time = om.duration
intro_video_time = intro_vid.duration
water_time = water.duration
tape_time = tape.duration
kaarthika_1_time = kaarthika_1.duration

#water
#water_ny, water_cville, water_houston, water_scotland, water_sf
water1 = water.subclip(0,2)
water2 = water.subclip(2,5)
#water_ny = water_ny.set_audio(CompositeAudioClip([water2.audio, ny]))

cville_txt = TextClip("centerville, ohio", fontsize=20, color='black', bg_color='white')

# setting position of text in the center and duration will be 10 seconds
cville_txt = cville_txt.set_pos((water.size[0]/4, water.size[1]/2)).set_duration(water2.duration)
cville = cville.subclip(1, water2.duration+1)
cville = cville.resize(0.4)
cville = cville.set_pos((water.size[0]/2, water.size[1]/4))
water_cville = CompositeVideoClip([water2, cville, cville_txt], size=(1920,1080), bg_color='black', use_bgclip=True, ismask=False)
#water_cville.audio = CompositeAudioClip([water3.audio, cville])
water3 = water.subclip(7,9)
houston_txt = TextClip("houston, texas", fontsize=20, color='black', bg_color='white')
houston_txt = houston_txt.set_pos((water.size[0]/2, water.size[1]/4)).set_duration(water3.duration)
houston = houston.subclip(1, 3)
houston = houston.resize(0.5)
houston = houston.set_pos((water.size[0]/4, water.size[1]/2))
water_houston = CompositeVideoClip([water3, houston, houston_txt], size=(1920,1080), bg_color='black', use_bgclip=True, ismask=False)
#water_houston.audio = CompositeAudioClip([water4.audio, houston])
water4 = water.subclip(9,12)
scotland_txt = TextClip("edinburgh, scotland", fontsize=20, color='black', bg_color='white')
scotland_txt = scotland_txt.set_pos((water.size[0]/4, water.size[1]/6)).set_duration(water4.duration)
scotland = scotland.subclip(0, water4.duration)
scotland = scotland.resize(0.4)
scotland = scotland.set_pos((water.size[0]/6, water.size[1]/4))
water_scotland = CompositeVideoClip([water4, scotland, scotland_txt], size=(1920,1080), bg_color='black', use_bgclip=True, ismask=False)
#water_scotland.audio = CompositeAudioClip([water5.audio, scotland])
water5 = water.subclip(12,15)
sf_txt = TextClip("san francisco, california", fontsize=20, color='black', bg_color='white')
sf_txt = sf_txt.set_pos((water.size[0]/6, water.size[1]/2)).set_duration(water5.duration)
sf = sf.subclip(0, water5.duration)
sf = sf.resize(0.4)
sf = sf.set_pos((water.size[0]/4, water.size[1]/6))
water_sf = CompositeVideoClip([water5, sf, sf_txt], size=(1920,1080), bg_color='black', use_bgclip=True, ismask=False)
water6 = water.subclip(15,18)
ny_txt = TextClip("new york, new york", fontsize=20, color='black', bg_color='white')
ny_txt = ny_txt.set_pos((water.size[0]/2, water.size[1]/2)).set_duration(water6.duration)
water_ny = CompositeVideoClip([water6, ny_txt], size=(1920,1080), bg_color='black', use_bgclip=True, ismask=False)
water_ny.audio = water6.audio
water7 = water.subclip(18,20)

#water_sf.audio = CompositeAudioClip([water6.audio, sf])


#intro + intro sound = first 5 seconds
intro_audioclip = CompositeAudioClip([intro_vid.audio, intro_sound])
intro_vid_1 = intro_vid.subclip(0, intro_sound_time)
intro_vid_1.audio = intro_audioclip
intro_sound_clip = intro_vid_1.subclip(0,5)

#tape + scrolling segment
bg_vid = intro_vid_1.subclip(5, intro_vid_1.duration)
#get tape subclip
tape_clip_length = bg_vid.duration + kaarthika_1_time
tape_start = random.randint(0, int(tape_time - tape_clip_length - 2))
tape = tape.subclip(tape_start, tape_start+tape_clip_length + 2)
#tape scrolling subclip
tape_scroll = tape.subclip(0, bg_vid.duration)
tape_scroll = tape_scroll.resize(0.4)
tape_scroll = tape_scroll.set_pos((bg_vid.size[0]/4, bg_vid.size[1]/4))
#tape_scroll = moviepy.video.fx.all.scroll(tape_scroll, x_speed=5)
tape_intro = CompositeVideoClip([bg_vid, tape_scroll], size=(1920,1080), bg_color='black', use_bgclip=True, ismask=False)
tape_intro.audio = bg_vid.audio

#tape_fullscreen
tape_full = tape.subclip(bg_vid.duration, tape.duration)
tape_full_slow = tape_full.fx( vfx.speedx, 0.25)
tape_full_final = tape_full_slow.subclip(0,2)


#tape_kaarthika
tape_kaarthika = tape_full_slow.subclip(2, kaarthika_1.duration+2)
self_1 = self_1.set_duration(tape_kaarthika.duration)
self_1 = self_1.set_pos((tape_full_slow.size[0]/4, tape_full_slow.size[1]/4))
self_1 = self_1.resize(0.2)
kaarthika_tape = CompositeVideoClip([tape_kaarthika, self_1])
kaarthika_tape.audio = kaarthika_1

#film in 3 parts
# film_sub = film.subclip(0, film.duration - 10)
# #film_one = moviepy.video.fx.all.accel_decel(film_sub, abruptness=1.0, soonness=1.0)
# #film_one.audio = film_sub.audio
#
#
#
# film_two = film.subclip(film.duration - 10, film.duration)
# other_1 = other_1.set_duration(film_two.duration)
# other_1 = other_1.resize(0.2).set_pos((700,0))
# film_two_final = CompositeVideoClip([film_two, other_1])
# film_two_final.audio = film_two.audio


other_2 = other_2.resize(tape.size)
other_breath = other_2.set_audio(breath).set_duration(breath.duration)
other_breath_one = other_breath.subclip(0, breath.duration/2)
other_breath_two = other_breath.subclip(breath.duration/2, breath.duration)
other_3 = other_3.set_duration(other_breath_two.duration)
other_3 = other_3.resize(0.2)
other_3 = other_3.set_pos((other_breath_two.size[0]/4, other_breath_two.size[1]/4))
breath_overlay = CompositeVideoClip([other_breath_two, other_3])
breath_overlay.audio = other_breath_two.audio

#spying
spying_clip = moviepy.video.fx.all.accel_decel(igstories, new_duration=spying.duration, abruptness=1.0, soonness=1.0)
spying_clip.audio = spying


#water
#water.audio = om


#kaarthika_again
# self_2 = self_2.set_duration(igstories.duration)
# self_2 = self_2.set_pos((igstories.size[0]/4, igstories.size[1]/4))
# self_2 = self_2.resize(0.2)
# kaarthika_vid = CompositeVideoClip([igstories, self_2]).subclip(0, kaarthika_2.duration)
# kaarthika_vid.audio = kaarthika_2


# other_1 = other_1.resize(0.2)
# other_1 = other_1.set_pos((0, 0))
# other_2 = other_2.set_duration(film.duration)
# other_2 = other_2.resize(0.2)
# other_2 = other_2.set_pos((0, tape_full_slow.size[1]-other_2.size[1])).set_duration(film.duration)
# film_final = CompositeVideoClip([film, other_1])




#make composite clip

#tape_scroll.set_position(lambda t: ('center', 500 + (1080-500)*(t/5)))

#tape_scroll = tape_scroll.fx(vfx.scroll, None, None, -5, 0, 1920, 1080/2,)



#tape full
#tape_full.audio = kaarthika_1




#concatanate + write to file
#
finalvid = concatenate_videoclips([intro_sound_clip, tape_intro, tape_full_final, kaarthika_tape, film, spying_clip, other_breath_one, breath_overlay, water1, water_cville, water_houston, water_scotland, water_sf, water_ny, water7], method='compose')
#finalvid = concatenate_videoclips([water1, water_cville, water_houston, water_scotland, water_sf, water6], method='compose')

finalvid.write_videofile("meettheparticipants.mp4", temp_audiofile='temp-audio.m4a', remove_temp=True, codec="libx264", audio_codec="aac")



#fl = lambda gf,t : gf(t)[int(t):int(t)+50, :]
#newclip = clip.fl(fl, apply_to='mask')





# clip = clip.resize(lambda t : 1+0.02*t) # slow swelling of the clip

#introduce randomness here
#clip = moviepy.video.fx.all.accel_decel(clip, abruptness=5.0, soonness=1.0)



#print("tape/")

#tape = VideoFileClip("tape.mp4")

## this is where we can change the speed

#picking a random sublicp for take, subtracting audiotime because we don't want to overshoot
#tapestart = random.randint(0, int(tape.duration - audiotime))

#tape = tape.subclip(tapestart, tapestart+audiotime)

#tape = tape.resize(0.8)

#tape = tape.set_pos((100,400))



#newclip = CompositeVideoClip([clip, tape], size=(1920,1080), bg_color='black', use_bgclip=True, ismask=False)

#fl = lambda gf,t : gf(t)[int(t):int(t)+50, :]
#newclip = newclip.fl(fl, apply_to='mask')




#newclip.audio = audioclip
#newclip = newclip.subclip(0, audiotime)




#tape.crossfadein(10)


# saving the clip
#newclip.write_videofile("attempt.mp4", temp_audiofile='temp-audio.m4a', remove_temp=True, codec="libx264", audio_codec="aac")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# loading video dsa gfg intro video
#clip = VideoFileClip("raw data thief cut.mov")

# clipping of the video
# getting video for only starting 10 seconds
#clip = clip.subclip(30, 40)

# rotating video by 180 degree
#clip = clip.rotate(180)


# saving the clip
#clip.write_videofile("final.mp4", temp_audiofile='temp-audio.m4a', remove_temp=True, codec="libx264", audio_codec="aac")
