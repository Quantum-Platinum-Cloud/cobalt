# Copyright 2014 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# This file is meant to be included by a GYP target that needs to copy the
# platform specific font data into <(PRODUCT_DIR)/content.

{
  'includes': [ '../build/contents_dir.gypi' ],
  'variables': {
    'source_all_fonts_dir': '<(static_contents_source_dir)/fonts/all_fonts',
  },

  'copies': [
    {
      'destination': '<(static_contents_output_data_dir)/fonts/',
      'files': [
        '<(static_contents_source_dir)/fonts/<(cobalt_font_package)/fonts.xml',
      ],
      'conditions': [
        [ 'cobalt_font_package == "minimal"', {
          'files+': [
            '<(source_all_fonts_dir)/MinimalRoboto.ttf',
            '<(source_all_fonts_dir)/CarroisGothicSC-Regular.ttf',
          ],
        }], # minimal
        [ 'cobalt_font_package == "10megabytes"', {
          'files+': [
            '<(source_all_fonts_dir)/NotoSansTagbanwa-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansSinhala-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansNewTaiLue-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansSundanese-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansMandaic-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansGurmukhiUI-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansDevanagariUI-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansMongolian-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansBamum-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansBuhid-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansCherokee-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansArmenian-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansJP-Regular.otf',
            '<(source_all_fonts_dir)/NotoSansEthiopic-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansGlagolitic-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansBatak-Regular.ttf',
            '<(source_all_fonts_dir)/Roboto-Regular.ttf',
            '<(source_all_fonts_dir)/NotoNaskhArabicUI-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansBuginese-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansVai-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansTifinagh-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansCham-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansJavanese-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansTeluguUI-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansTaiLe-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansMeeteiMayek-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansKannadaUI-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansSyriacEstrangela-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansBengaliUI-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansThaiUI-Regular.ttf',
            '<(source_all_fonts_dir)/CarroisGothicSC-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansNKo-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansGeorgian-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansSymbols-Regular-Subsetted.ttf',
            '<(source_all_fonts_dir)/NotoSansCoptic-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansYi-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansTaiTham-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansOlChiki-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansOriyaUI-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansSylotiNagri-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansRejang-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansCanadianAboriginal-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansLisu-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansTibetan-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansKayahLi-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansLaoUI-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansHanunoo-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansTaiViet-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansHebrew-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansBalinese-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansTamilUI-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansGujaratiUI-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansMalayalamUI-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansLepcha-Regular.ttf',
            '<(source_all_fonts_dir)/NotoEmoji-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansThaana-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansKhmerUI-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansSaurashtra-Regular.ttf',
            '<(source_all_fonts_dir)/DroidSansFallback.ttf',
            '<(source_all_fonts_dir)/NotoSansLimbu-Regular.ttf',
          ],
        }], # 10megabytes
        [ 'cobalt_font_package == "unlimited"', {
          'files+': [
            '<(source_all_fonts_dir)/NotoSansTagbanwa-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansSinhala-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansNewTaiLue-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansSundanese-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansMandaic-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSerif-Bold.ttf',
            '<(source_all_fonts_dir)/NotoSansTeluguUI-Bold.ttf',
            '<(source_all_fonts_dir)/NotoSansMyanmarUI-Bold.ttf',
            '<(source_all_fonts_dir)/NotoSansGurmukhiUI-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansDevanagariUI-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansMongolian-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansArmenian-Bold.ttf',
            '<(source_all_fonts_dir)/NotoSansBamum-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansBuhid-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansEthiopic-Bold.ttf',
            '<(source_all_fonts_dir)/NotoSansDevanagariUI-Bold.ttf',
            '<(source_all_fonts_dir)/NotoSansCherokee-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansArmenian-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansJP-Regular.otf',
            '<(source_all_fonts_dir)/NotoSansOriyaUI-Bold.ttf',
            '<(source_all_fonts_dir)/NotoSansEthiopic-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansGlagolitic-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansBatak-Regular.ttf',
            '<(source_all_fonts_dir)/Roboto-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansTC-Regular.otf',
            '<(source_all_fonts_dir)/NotoSerif-Regular.ttf',
            '<(source_all_fonts_dir)/NotoNaskhArabicUI-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansBuginese-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansVai-Regular.ttf',
            '<(source_all_fonts_dir)/MTLmr3m.ttf',
            '<(source_all_fonts_dir)/NanumGothic.ttf',
            '<(source_all_fonts_dir)/ComingSoon.ttf',
            '<(source_all_fonts_dir)/NotoSansTifinagh-Regular.ttf',
            '<(source_all_fonts_dir)/DancingScript-Bold.ttf',
            '<(source_all_fonts_dir)/NotoSansCham-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansSC-Regular.otf',
            '<(source_all_fonts_dir)/NotoSansHebrew-Bold.ttf',
            '<(source_all_fonts_dir)/NotoSansJavanese-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansTeluguUI-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansTaiLe-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansMeeteiMayek-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansKannadaUI-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansKhmerUI-Bold.ttf',
            '<(source_all_fonts_dir)/NotoSansSyriacEstrangela-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSerif-BoldItalic.ttf',
            '<(source_all_fonts_dir)/NotoSansBengaliUI-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansThaiUI-Regular.ttf',
            '<(source_all_fonts_dir)/CutiveMono.ttf',
            '<(source_all_fonts_dir)/DroidSansMono.ttf',
            '<(source_all_fonts_dir)/CarroisGothicSC-Regular.ttf',
            '<(source_all_fonts_dir)/Roboto-Italic.ttf',
            '<(source_all_fonts_dir)/NotoSansNKo-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansGeorgian-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansSymbols-Regular-Subsetted.ttf',
            '<(source_all_fonts_dir)/NotoSansCoptic-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansYi-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansTaiTham-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansMyanmarUI-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansMalayalamUI-Bold.ttf',
            '<(source_all_fonts_dir)/NotoSansGujaratiUI-Bold.ttf',
            '<(source_all_fonts_dir)/NotoSansLaoUI-Bold.ttf',
            '<(source_all_fonts_dir)/NotoSansOlChiki-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansOriyaUI-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansSylotiNagri-Regular.ttf',
            '<(source_all_fonts_dir)/Roboto-Bold.ttf',
            '<(source_all_fonts_dir)/NotoSansRejang-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansThaiUI-Bold.ttf',
            '<(source_all_fonts_dir)/NotoSansCanadianAboriginal-Regular.ttf',
            '<(source_all_fonts_dir)/Roboto-BoldItalic.ttf',
            '<(source_all_fonts_dir)/NotoSansLisu-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansTibetan-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansKayahLi-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansLaoUI-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansHanunoo-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansTaiViet-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansKannadaUI-Bold.ttf',
            '<(source_all_fonts_dir)/NotoSansSinhala-Bold.ttf',
            '<(source_all_fonts_dir)/NotoSerif-Italic.ttf',
            '<(source_all_fonts_dir)/NotoSansGurmukhiUI-Bold.ttf',
            '<(source_all_fonts_dir)/NotoSansHebrew-Regular.ttf',
            '<(source_all_fonts_dir)/DancingScript-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansBalinese-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansTamilUI-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansGujaratiUI-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansGeorgian-Bold.ttf',
            '<(source_all_fonts_dir)/NotoSansMalayalamUI-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansLepcha-Regular.ttf',
            '<(source_all_fonts_dir)/NotoEmoji-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansTamilUI-Bold.ttf',
            '<(source_all_fonts_dir)/NotoSansThaana-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansKhmerUI-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansSaurashtra-Regular.ttf',
            '<(source_all_fonts_dir)/NotoSansKR-Regular.otf',
            '<(source_all_fonts_dir)/NotoSansCham-Bold.ttf',
            '<(source_all_fonts_dir)/DroidSansFallback.ttf',
            '<(source_all_fonts_dir)/NotoSansBengaliUI-Bold.ttf',
            '<(source_all_fonts_dir)/MinimalRoboto.ttf',
            '<(source_all_fonts_dir)/NotoSansLimbu-Regular.ttf',
            '<(source_all_fonts_dir)/NotoNaskhArabicUI-Bold.ttf',
            '<(source_all_fonts_dir)/NotoSansThaana-Bold.ttf',
          ],
        }], # unlimited
      ],
    },
  ],
}