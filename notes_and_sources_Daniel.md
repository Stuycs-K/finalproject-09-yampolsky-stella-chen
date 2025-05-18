# Columnar Transposition Cipher
## The Columnar Part
The Columnar cipher is a cipher that rearranges plaintext so that it looks quite weird. However, it doesn't change the actual letters like a Caesar Cipher or any polyalphabetic cipher. 

## Example of the Columnar Part
We have this sentence. Let's say the key length was 5. Exclude the spaces and the cipher text would be:<br/>
<br/>
Wehav<br/>
ethis<br/>
sente<br/>
nce<br/>

If the length of the plaintext is not divisible by the key length, then just add nulls (spaces).

## The Transposition Part
Transpositioning is when the columns of a columnar cipher gets switched.
Going back to the previous cipher, if we have the keyword zebra, we have the first column
be z, second e, third b, fourth r, fifth a. Now, we order based on alphabetical order, which is a, b, e, r, and z. This means it becomes <br/>
</br>
vheaW</br>
shtie</br>
enets</br>
 ec n</br>

