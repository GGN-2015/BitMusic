FFMPEG = ffmpeg
OUTPUT = output.wav
MLIST  = MergeList.txt

$(OUTPUT): $(MLIST)
	$(FFMPEG) -f concat -i $(MLIST) -c copy $(OUTPUT)

clean:
	rm $(OUTPUT)

.PHNOY: clean
	
