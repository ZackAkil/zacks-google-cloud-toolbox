# pip install google-cloud-texttospeech

from google.cloud import texttospeech

def generate_speech_mp3(script, output_file_name="output.mp3", rate=1):

    tts_client = texttospeech.TextToSpeechClient()
  
    synthesis_input = texttospeech.SynthesisInput(text=script)

    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US", name='en-US-Studio-O'
    )

    # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
        speaking_rate=rate 
    )

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    tts_response = tts_client.synthesize_speech(input=synthesis_input, 
                                                     voice=voice, 
                                                     audio_config=audio_config)
    with open(output_file_name, "wb") as out:
        # Write the response to the output file.
        out.write(tts_response.audio_content)
        print(f'Audio content written to file: {output_file_name}')
      
    return output_file_name
