[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/am3xLbu5)
# This is the only project.
 
### Members

Daniel Chen and Stella Yampolsky
       
### Project Description:

This project explains what the Hill Cipher and Columnar Transposition Cipher is, some advantages/disadvantages, some history if there is available. 
  
### Instructions:

The user uses the makefile and make compiler to compile this program. For the Column encode, the parameters are (plaintext, keyword, printstyle) while for the Column decode, the parameters are (ciphertext, keyword). The plaintext is the text the user wants to encode. The keyword is the keyword that will help with encoding and decoding. The ciphertext is the encoded text. Printstyle is for encode only, where the user can either print the ciphertext in a column or in a linear text. The column text is better used to visualize how the transposition columnar cipher swaps everything while the linear text style is best if the user wants to decode a ciphertext.  
</br>
Here are example makefile command arguments for the Columnar Transposition Cipher:
```
make encodeColumnar ARGS="'I have this sentence.' humor column"
make encodeColumnar ARGS="'I have this sentence.' humor lienar"
make decodeColumnar ARGS="'Iavehtisshetennc   e' humor"
```

For the Hill encode, [INPUT STUFF HERE] while for the Hill decode, [INPUT STUFF HERE].


### Resources/ References:

Transposition cipher Wikipedia: [Transposition Cipher](https://en.wikipedia.org/wiki/Transposition_cipher)</br>
The Columnar Transposition Cipher Video: [The Columnar Transposition Cipher Explained and Broken](https://www.youtube.com/watch?v=FM50lnSC51c)</br>
Advantages and Disadvantages of Transposition Columnar Cipher: [Hill Cipher](https://prezi.com/tzjqqlhkkvxf/columnar-transposition/)</br>
Columnar Cipher Decoder: [Columnar Cipher Decoder](https://www.dcode.fr/columnar-transposition-cipher)</br>
Hill Cipher Matrix Tutorial: [Hill Cipher](https://massey.limfinity.com/207/hillcipher.pdf)</br>
Hill Cipher Wikipedia: [Wikipedia](https://en.wikipedia.org/wiki/Hill_cipher)</br>
Hill Cipher Encoder and Decoder Website: [Hill Cipher Website](https://massey.limfinity.com/207/hillcipher.php)
* Julien and Jakob aided with linear algebra topics like matrices
