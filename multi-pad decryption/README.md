# Multi-pad decryption

The main idea is that when you XOR a small letter and a space, you can obtain the same capital letter.
When you XOR a capital letter and a space, you can obtain the lowercase version. <return>
I provide two version of decryption codes here. "decode_accurate()" can detect the space positions
in every cipertext but may provide little clues for us to guess.
"decode_rough()" ignore other characters besides letters and space.
Therefore it may provide lots of letters but some of them are incorrect.
I usually combine these two methods together to decrypt.