// Copyright 2015 Google Inc. All Rights Reserved.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

// Definition of input events and associated data types.

#ifndef STARBOARD_INPUT_H_
#define STARBOARD_INPUT_H_

#include "starboard/configuration.h"
#include "starboard/export.h"
#include "starboard/key.h"
#include "starboard/types.h"
#include "starboard/window.h"

#ifdef __cplusplus
extern "C" {
#endif

// All possible input subsystem types.
typedef enum SbInputDeviceType {
  // Input from some gesture-detection mechanism. Examples include Kinect,
  // Wiimotes, LG Magic Remotes, etc...
  //
  // Produces Move, Grab, Ungrab, Press and Unpress events.
  kSbInputDeviceTypeGesture,

  // Input from a gamepad, following the layout provided in the W3C Web Gamepad
  // API.
  //
  // Produces Move, Press and Unpress events.
  kSbInputDeviceTypeGamepad,

  // Keyboard input from a traditional keyboard, or game controller chatpad.
  //
  // Produces Press and Unpress events.
  kSbInputDeviceTypeKeyboard,

  // Input from a microphone that would provide audio data to the caller, who
  // may then find some way to detect speech or other sounds within it. It may
  // have processed or filtered the audio in some way before it arrives.
  //
  // Produces Audio events.
  kSbInputDeviceTypeMicrophone,

  // Input from a traditional mouse.
  //
  // Produces Move, Press, and Unpress events.
  kSbInputDeviceTypeMouse,

  // Input from a TV remote control-style device.
  //
  // Produces Press and Unpress events.
  kSbInputDeviceTypeRemote,

  // Input from a speech command analyzer, which is some hardware or software
  // that, given a set of known phrases, activates when one of the registered
  // phrases is heard.
  //
  // Produces Command events.
  kSbInputDeviceTypeSpeechCommand,

  // Input from a single- or multi-touchscreen.
  //
  // Produces Move, Press, and Unpress events.
  kSbInputDeviceTypeTouchScreen,

  // Input from a touchpad that isn't masquerading as a mouse.
  //
  // Produces Move, Press, and Unpress events.
  kSbInputDeviceTypeTouchPad,
} SbInputType;

// The action that an input event represents.
typedef enum SbInputEventType {
  // Receipt of Audio. Some audio data was received by the input microphone.
  kSbInputEventTypeAudio,

  // Receipt of a command. A command was received from some semantic source,
  // like a speech recognizer.
  kSbInputEventTypeCommand,

  // Grab activation. In some gesture systems a grab gesture is dfferent from an
  // activate gesture. An Ungrab event will follow when the grab gesture is
  // terminated.
  kSbInputEventTypeGrab,

  // Device Movement. In the case of Mouse, and perhaps Gesture, the movement
  // tracks an absolute cursor position. In the case of TouchPad, only relative
  // movements are provided.
  kSbInputEventTypeMove,

  // Key or button press activation. This could be a key on a keyboard, a button
  // on a mouse or game controller, or a push from a touch screen or gesture. An
  // Unpress event will be delivered once the key/button/finger is
  // raised. Injecting repeat presses is up to the client.
  kSbInputEventTypePress,

  // Grab deactivation. An Ungrab event will be sent when a grab gesture is
  // terminated.
  kSbInputEventTypeUngrab,

  // Key or button deactivation. The counterpart to the Press event, this event
  // is sent when the key or button being pressed is released.
  kSbInputEventTypeUnpress,
} SbInputEventType;

// A 2-dimensional vector used to represent points and motion vectors.
typedef struct SbInputVector {
  int x;
  int y;
} SbInputVector;

// Event data for kSbEventTypeInput events.
typedef struct SbInputData {
  // The window that this input was generated at.
  SbWindow window;

  // The type of input event this represents.
  SbInputEventType type;

  // The type of device that generated this input event.
  SbInputDeviceType device_type;

  // An identifier unique amongst all connected devices.
  int device_id;

  // An identifier that indicates which keyboard key or mouse button was
  // involved in this event, if any. All known keys for all devices are mapped
  // to a single ID space, defined by the enum SbKey in key.h.
  SbKey key;

  // The character that corresponds to the key. For an external keyboard, this
  // character also depends on the language of keyboard type. Will be 0 if there
  // is no corresponding character.
  wchar_t character;

  // The location of the specified key, in cases where there are multiple
  // instances of the button on the keyboard. The "shift" key, for example.
  SbKeyLocation key_location;

  // Key modifiers (e.g. Ctrl, Chift) held down during this input event.
  unsigned int key_modifiers;

  // The (x, y) coordinates of the persistent cursor controlled by this
  // device. Will be 0 if not applicable.
  SbInputVector position;

  // The relative motion vector of this input. Will be 0 if not applicable.
  SbInputVector delta;
} SbInputData;

#ifdef __cplusplus
}  // extern "C"
#endif

#endif  // STARBOARD_INPUT_H_