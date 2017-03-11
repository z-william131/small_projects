# small_projects

Here are some of the small projects that I am working on in recent years.

## multi-pad decryption

I built this project when I studied computer security in 2017. 
I learned about the One Time Pad (OTP) and Stream Ciphers, a practical form of using OTPs for encryption.
As the name suggests, a one time pad should only ever be used once when encrypting messages.

For this project, I try to explore what will go wrong if the same keystream (pad) is used multiple times to encrypt messages.

## FileSort

The FiltSort function requires an input: the path to a folder,and then it will generate an output.txt file that includes
the "index, file name, address, maintag, subtag, subtag2" of every file in that folder. It can also return the output file as a list.
The tags will be the name of every subfolder's name.

For example, The struction of folder "Hobbies" is like this:

1. Sports
  * Basketball -- Some articles about basketball
  * Football -- Some articles about football
2. Arts
  * Watercolor
  * Comic
3. Music

And the result will be 

[[1, article1, /sports/basketball/artical1, sports, basketball, None],

[2, article2, /sports/football/artical2, sports, football, None],

[3, article3, /Arts/watercolor/artical3, arts, watercolor, None],

[4, article4, /Arts/comic/artical4, arts, comic, None], ... ]

## Confusion Matrix

The basic struction for machine learning
