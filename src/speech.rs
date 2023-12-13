extern crate whisper;
extern crate tts;

use whisper::Whisper;
use tts::Tts;

pub struct Speech {
    whisper: Whisper,
    tts: Tts,
}

impl Speech {
    pub fn new() -> Self {
        Self {
            whisper: Whisper::new(),
            tts: Tts::new(),
        }
    }

    pub fn speech_to_text(&self, audio_data: &[u8]) -> Result<String, Box<dyn std::error::Error>> {
        // TODO: Implement this method
        unimplemented!()
    }

    pub fn text_to_speech(&self, text: &str) -> Result<Vec<u8>, Box<dyn std::error::Error>> {
        // TODO: Implement this method
        unimplemented!()
    }
}