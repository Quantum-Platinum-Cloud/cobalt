// Copyright 2016 Google Inc. All Rights Reserved.
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

// Here we are not trying to do anything fancy, just to really sanity check that
// this is hooked up to something.

#include "starboard/system.h"
#include "testing/gtest/include/gtest/gtest.h"

namespace starboard {
namespace nplb {
namespace {

TEST(SbSystemHasCapabilityTest, SunnyDay) {
  // Ensure that this doesn't crash, but we don't know if it should legitimately
  // be true or false.
  SbSystemHasCapability(kSbSystemCapabilityReversedEnterAndBack);
  SbSystemHasCapability(kSbSystemCapabilityCanQueryGPUMemoryStats);
}

TEST(SbSystemHasCapabilityTest, SunnyDayNoChange) {
  bool a;

  a = SbSystemHasCapability(kSbSystemCapabilityReversedEnterAndBack);
  EXPECT_EQ(a, SbSystemHasCapability(kSbSystemCapabilityReversedEnterAndBack));

  a = SbSystemHasCapability(kSbSystemCapabilityCanQueryGPUMemoryStats);
  EXPECT_EQ(a,
            SbSystemHasCapability(kSbSystemCapabilityCanQueryGPUMemoryStats));
}

TEST(SbSystemHasCapabilityTest, RainyDayNoSuchCapability) {
  EXPECT_FALSE(SbSystemHasCapability(static_cast<SbSystemCapabilityId>(99999)));
}

}  // namespace
}  // namespace nplb
}  // namespace starboard