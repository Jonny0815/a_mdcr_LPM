import Live
from _Framework.ControlSurface import ControlSurface
from _Framework.Layer import Layer
from _Framework.DeviceComponent import DeviceComponent
from _Framework.MixerComponent import MixerComponent
from _Framework.SliderElement import SliderElement
from _Framework.TransportComponent import TransportComponent
from _Framework.InputControlElement import *
from _Framework.ButtonElement import ButtonElement
from _Framework.ButtonMatrixElement import ButtonMatrixElement
from _Framework.SessionComponent import SessionComponent
from _Framework.EncoderElement import *
from _Framework.SliderElement import SliderElement
from _Framework.SubjectSlot import SlotManager, subject_slot
from _Framework.EncoderElement import EncoderElement
from _Framework.ToggleComponent import ToggleComponent
from .ToggleButton import ToggleButton
from functools import partial
import time
from itertools import chain
from _Framework.Util import find_if
import collections
import json

from typing import Dict, List, Optional

session: Optional[SessionComponent] = None
mixer: Optional[MixerComponent] = None


class Mdcr_LPM(ControlSurface):
    def __init__(self, c_instance):
        super(Mdcr_LPM, self).__init__(c_instance)
        with self.component_guard():
            self.current_track_offset = 0
            self.current_scene_offset = 0
            num_tracks = 8
            num_returns = 2
            # self._fcb: Fcb = Fcb(self)
            # self.mixer.channel_strip(0).set_volume_control(EncoderElement(MIDI_CC_TYPE, 8, 1, Live.MidiMap.MapMode.absolute))
            # self.mixer.channel_strip(0).set_volume_control(self._bcf.faders[0])
            self.test_listener.subject = ButtonElement(True, MIDI_CC_TYPE, 3, 40)
            # self.mixer.channel_strip(0).set_mute_button(ToggleButton(True, MIDI_CC_TYPE, 16, 73, c_instance))
            # self.mixer.channel_strip(0).set_mute_button(self._bcf._buttons[1][0])

    @subject_slot("value")
    def test_listener(self, value):
        self.show_message("test listener")

    def disconnect(self):
        super(Mdcr_LPM, self).disconnect()
