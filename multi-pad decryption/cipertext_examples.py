# Examples of cipertexts and target

Ciphertext1 = "9dc26aa8bc3f39ba761ea6f583e705a9d1c7f2da07301c004812f2e914361f73361645611785f8b6a9d2af7083e0c70eb2abf14d10de3ce52bceac79a90dc24fe74b06838365"
Ciphertext2 = "9dc26aa8b43d27b6701ea6a6c7ea09bb9fd0e494077818020d19e4e85c3e137b6404177715d0fefea19bb46a8eebcc40e69db8402ccb34ad68cea47ae71bc102f6045f958b658551"
Ciphertext3 = "9ecf2fe6b43533f3761ef4edcaeb0abb8194e3dc126459124c12e5bd083a10777e1959695ac4ffada581b37889f08217fa9db84f3a9f21a03adfed64b218cb1db34552da8f628e55584f"
Ciphertext4 = "808a7ce9a67023bb6305f4f2cbea44bf9cc4fec616300a1e5814eff20b3151557814456114ccefb1bfd2a67783a4cf09f59aec062bda77b620d3b963ae06c94ff74b5194cc54b9640c6c173ce744f6"
Ciphertext5 = "86c22fe6be7039bc765190c8e2af28b584daf0d1536411175913abea143a037136045f6b5ad5e3aebc9ba97ec7e7ce15f0d2fb4725d332a168e4a278b301cb4ffa57"
Ciphertext6 = "8cdc6afaa83238b77b51a7f2ccff44ae90d8fcdd1d7759184217aabd5c7f51343650172e3385f8b6a59cac3993eccb13f19af94827da3bad29d5ed75a20dc00de1414799847593"
Ciphertext7 = "9ac363edbf3332f3221ebaa6d7e701fa86dde5d1533058560d40c8f515331566731e1a475ad6edb7a8d2b4708be1cc03f7d2b806699f77e568869e63a8188e4fb30406da98719b4e454e1f"
Ciphertext8 = "e98a2fa8953f77aa6d04f4e3d5ea0afa9dddf1c053720b174540cff4187f087b63505c6015d2acaaa497e74fb7a4cb13b286f04369d025ac2fcfa376ab48ec1dfc43549b817d9257"
Ciphertext9 = "9bcf6ee4f13325aa7205bbe1d1ee14b294c6e494077f0d17410cf2bd1830517a7904176514cafbfea49db03993eb8215e197b8760eef77b120c7b964af1dc30efd424799987f855658551e2fa95afc"
Target = "84d32feebe2223a16702a7a6c1e311bf81c6feda076359175f05abe8123b146636045f6b5adce3b9b980b33994e1c114fb9df60620d177872dd4a672ab0dd74fd14b5196"

ciphers = [Ciphertext1, Ciphertext2, Ciphertext3, Ciphertext4, Ciphertext5, Ciphertext6, Ciphertext7, Ciphertext8, Ciphertext9]

print(decode_accurate(ciphers, target))
print(decode_accurate(ciphers, target))

print("The decrypted target cipertext is 'My fortress blueprint are under the yogurt section in Berkelely Bowl.'")