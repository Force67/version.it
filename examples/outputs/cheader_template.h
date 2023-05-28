#ifndef VERSION_IT_INCLUDE_GUARD
#define VERSION_IT_INCLUDE_GUARD
#define VERSION_IT_VERSION "1.33.266"
#define VERSION_IT_USING_SEMANTIC_VERSIONING
#define VERSION_IT_MAJOR 1
#define VERSION_IT_MINOR 33
#define VERSION_IT_PATCH 266

#ifdef __cplusplus
namespace version_it
{
  constexpr const char kVersionString[] = "1.33.266";
  constexpr int major = 1;
  constexpr int minor = 33;
  constexpr int patch = 266;
}
#endif

#ifdef __cplusplus
namespace version_it
{
  static inline const char* kChangelogEntries[59] =
  {
    "unittests",
    "cleanup",
    "c",
    "current_branch",
    "a bunch of fixes",
    "Does that fix anything????",
    "some updates",
    "does this fix all of the things?",
    "attempt to fix history",
    "does that fix it?",
    "last tag assignment",
    "change commiter",
    "cleanup changes",
    "invalid URl",
    "big brain changes",
    "provide versioning scheme specific variables",
    "ci",
    "improve a bunch of jinja templates",
    "just instantiate the templating engine once. no more custom exporters.",
    "Implement jinja2 templating engine",
    "redo config unit test",
    "use gitpython instead of manual git invocation",
    "Implement hmtl changelog exporter",
    "improve exporters",
    "Improve cheader gen code.",
    "yeet custom logger",
    "support files named .yml for config",
    "add reqs",
    "add CI",
    "bandaid fix to restore functionality",
    "small code improvements",
    "assign right type",
    "switch to yaml for the config",
    "a tweak",
    "run-on",
    "adjust json exporter",
    "changes",
    "move outputs elsewhere",
    "configurable increment weights",
    "improve cheader exporter",
    "C Header exporter",
    "version.it test",
    "full history build mode",
    "update regex",
    "more options",
    "empty message",
    "test",
    "more questionable code",
    "test",
    "enable link embedding in markdown",
    "increase test cov",
    "final change for today!",
    "formatter & linter",
    "todo",
    "some change",
    "begin test coverage",
    "improve spec even moar",
    "some more documentation work",
    "refactor state"
  };
}
#endif

// 1.33.266 fix 61c59721d1bb3b3f9fa740a6412ba056c0483bc1 2023-05-28 Vincent Hengel unittests
// 1.33.265 tweak f4bd63e7209a67b6c50723d4a03f98817684abf9 2023-05-28 Vincent Hengel cleanup
// 1.33.264 tweak 676270dfc2756ec5062283f99d8b1e6753465f05 2023-05-27 Vincent Hengel c
// 1.33.263 fix c48889a3209bfe2ee6bc962989ae8619afd167b3 2023-04-24 Vincent Hengel current_branch
// 1.33.263 tweak fe94cc099a86cf237e015b0310c2e54c0c151872 2023-04-24 Vincent Hengel a bunch of fixes
// 1.33.263 tweak bbebda091bf7340a63b9676640baab902105dd0f 2023-04-23 Vincent Hengel Does that fix anything????
// 1.33.263 fix 9674ccb5bf08e8fdab748ce09f325b8b8e9dd5cf 2023-04-22 Vincent Hengel some updates
// 1.33.263 tweak 8329adbe8e1e44ab0dc6c163801e8248cfc14ee7 2023-04-16 Vincent Hengel does this fix all of the things?
// 1.33.257 tweak 8e846f174764f6cfe0602973a0f6384727fd7407 2023-04-16 Vincent Hengel attempt to fix history
// 1.33.256 tweak 0b9bdf59fe399b0d9872174e7be7e047a64fed16 2023-04-16 Vincent Hengel does that fix it?
// 1.23.214 fix 0b6d52e7961f9b7773aed042b4dbb3d19f272a9c 2023-04-16 Vincent Hengel last tag assignment
// 1.13.174 tweak c132e1fc6779a0775cebaa191fa6eec5d77f4d29 2023-04-16 Vincent Hengel change commiter
// 1.13.174 tweak 585764ec08615c4c5a68dd2ce5ed6995beaa288b 2023-04-16 Vincent Hengel cleanup changes
// 1.13.174 fix d3b637cf08a592c6ec34cabbe56d7ab39e8b4a4e 2023-04-16 Vincent Hengel invalid URl
// 1.13.171 tweak 245abc040b7d501bf7b932fdaacd04e0d0675eb0 2023-04-16 Vincent Hengel big brain changes
// 1.13.171 tweak 6fc719ba485d1c651a095b789e95ad9db007442f 2023-04-16 Vincent Hengel provide versioning scheme specific variables
// 1.13.171 tweak fb4e96b024c101de4092e4782d5264904a6d3f36 2023-04-16 Vincent Hengel ci
// 1.13.171 feat 12a077d24fee09bf3afb55105bd71f107a8d6ea3 2023-04-16 Vincent Hengel improve a bunch of jinja templates
// 1.13.171 tweak 56063663bc8a12871de6891e99a6a7214af00a73 2023-04-16 Vincent Hengel just instantiate the templating engine once. no more custom exporters.
// 1.13.171 feat fb4f6beaed9658f2101e4200da4406771561b15b 2023-04-16 Vincent Hengel Implement jinja2 templating engine
// 1.13.171 tweak aba6ec9d686eccb153a4b542c6a62c5ede53d52d 2023-04-16 Vincent Hengel redo config unit test
// 1.13.171 tweak 4a403660f7d72d76457b6fe24162c498ff2a7073 2023-04-16 Vincent Hengel use gitpython instead of manual git invocation
// 1.13.171 feat 2fb6174e5145186cedd7a12f28cfc26c7315ede1 2023-04-16 Vincent Hengel Implement hmtl changelog exporter
// 1.13.171 tweak f50c82c22be20e7d01b51526b1de56534aed478f 2023-04-16 Vincent Hengel improve exporters
// 1.13.171 tweak(style) 1c7e9f6bdb71102b50053efc30214233e35aff09 2023-04-16 Vincent Hengel Improve cheader gen code.
// 1.13.171 tweak 678990fd83f15b628b41063b911178a8e418af28 2023-04-16 Vincent Hengel yeet custom logger
// 1.13.171 tweak 248ab4f31fee97f21aa18ad2aa04c874a77b9d99 2023-04-15 Vincent Hengel support files named .yml for config
// 1.13.171 tweak 95ad3ba2229b8482d6c3f902a250201951262f60 2023-03-27 Vincent Hengel add reqs
// 1.13.171 tweak 01439caf74e2b62fce0bfea74ba07b03f0460a6f 2023-03-27 Vincent Hengel add CI
// 1.13.171 fix 9f2242d228cd9e444dacaeb424edd13720869272 2023-03-27 Vincent Hengel bandaid fix to restore functionality
// 1.13.171 tweak 617efb86193d9e7457d11ba1364614a65c0cdb41 2023-03-14 Vincent Hengel small code improvements
// 1.13.171 fix a43e3cbd0e6bf0b100ac5429db9165f45a82bb25 2023-03-13 Vincent Hengel assign right type
// 1.13.171 feat 3f26e3d95c507cdeda50d4d065b3bc41a924dd7c 2023-03-13 Vincent Hengel switch to yaml for the config
// 1.13.171 tweak e39940603eab62e69193fba3dc0e7985328e8ed5 2023-02-25 Vincent Hengel a tweak
// 1.13.171 feat 03c78d2d08d826b1863dce5f77f6d38fb3a0bd04 2023-02-25 Vincent Hengel run-on
// 1.11.158 tweak 1c523102805167500e054db0bdb4bccadd84bc90 2023-02-14 Vincent Hengel adjust json exporter
// 1.11.156 tweak 8749c775dc20a63597243694c7c43867bf821514 2023-02-14 Vincent Hengel changes
// 1.8.155 refactor 3f9fdeb8ec029a5ae3fe1478b0d4bd84b74ee052 2023-02-07 Vincent Hengel move outputs elsewhere
// 1.8.155 feat 4ae59670943d87e4925961d9c7b72d54fdc58962 2023-02-05 Vincent Hengel configurable increment weights
// 1.8.155 feat 5d7fdfbdddee794ac2f60e2d2b7b43cc9bfacbb5 2023-02-05 Vincent Hengel improve cheader exporter
// 1.1.83 feat acc7372ae5d2306babc1b53495a85ea6d0e02b39 2023-02-04 Vincent Hengel C Header exporter
// 1.0.47 tweak 8e3bbde9307bb9ac0f4cc219cef6f10bd1b9934a 2023-02-03 Vincent Hengel version.it test
// 1.0.29 tweak 983b2f7d3dc9d6e92e02e9b4a71112e4e82d73da 2023-02-03 Vincent Hengel full history build mode
// 1.0.12 tweak d94fd4534d3b9b6dc4803a4a3c77be645d2bf7b1 2023-02-03 Vincent Hengel update regex
// 1.0.12 tweak 53f8648a403107b65d684dccfa779c164f5bb79e 2023-02-03 Vincent Hengel more options
// 1.0.12 tweak b19b9379244e28e6e04299768e0cf26cb48aac74 2023-02-02 Vincent Hengel empty message
// 1.0.9 fix 696a3565b43fd4885d5eca812d849d9efdbdc7c6 2023-01-29 Vincent Hengel test
// 1.0.8 tweak 9ef003aa04d889dde7908bb50aed1e21f647f80f 2023-01-28 Vincent Hengel more questionable code
// 1.0.8 tweak a2d2aa9007a8a4a46221c77449eee405d5b882f2 2023-01-28 Vincent Hengel test
// 1.0.8 tweak a13f0648ddd243ffb5483816d1b84d11ace46460 2023-01-28 Vincent Hengel enable link embedding in markdown
// 1.0.8 tweak 555abb42d36df2465f251a70049e7b61a1a538cf 2023-01-28 Vincent Hengel increase test cov
// 1.0.8 tweak a18880e940ddac50058766be550c628ae063ec3a 2023-01-26 Vincent Hengel final change for today!
// 1.0.8 style 7b810c55739dbc55bafc00a8b4e703874ce1d2c0 2023-01-26 Vincent Hengel formatter & linter
// 1.0.8 tweak 74ea18806c3a30fb05935f5e9fe94588c958b364 2023-01-25 Vincent Hengel todo
// 1.0.8 tweak 1bfe97c9ba54c72535fcb377ac47fccca12d5f20 2023-01-25 Vincent Hengel some change
// 1.0.0 tweak 00118340c6104071062fad1c4ee0625f8f520547 2023-01-25 Vincent Hengel begin test coverage
// 1.0.0 tweak be61abec0d0a71aa47d540650b0f55e737ef7935 2023-01-19 Vincent Hengel improve spec even moar
// 1.0.0 tweak 2d3765d6c03492ac554285e11583ce8109ac9cb1 2023-01-19 Vincent Hengel some more documentation work
// 1.0.0 tweak ffe0ece787de58076bb55fd6a0dc89b01430549b 2022-12-05 Vincent Hengel refactor state
#endif