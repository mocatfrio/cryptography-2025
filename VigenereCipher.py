# we need the alphabet because we convert letters into numerical values
# to be able to use mathematical operations (note we encrypt the spaces as well)
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def vigenere_encrypt(plain_text, key):
    # remove punctuation and make the text case-insensitive
    plain_text = ''.join(c for c in plain_text.upper() if c in ALPHABET)
    key = key.upper()

    cipher_text = ''
    # it represents the index of the letters of the key
    key_index = 0

    # we have to consider all the characters in the plain_text
    for character in plain_text:
        # number of shifts = index of the character in the alphabet +
        # index of the character in the key
        index = (ALPHABET.find(character)+ALPHABET.find(key[key_index])) % len(ALPHABET)
        # keep appending the encrypted character to the cipher_text
        cipher_text = cipher_text + ALPHABET[index]

        # increment the key index because we consider the next letter
        key_index = key_index + 1

        # if we've considered the last letter of the key we start again
        if key_index == len(key):
            key_index = 0

    return cipher_text


def vigenere_decrypt(cipher_text, key):
    # remove punctuation and make the text case-insensitive
    cipher_text = ''.join(c for c in cipher_text.upper() if c in ALPHABET)
    key = key.upper()

    plain_text = ''
    key_index = 0

    for character in cipher_text:
        index = (ALPHABET.find(character)-ALPHABET.find(key[key_index])) % len(ALPHABET)
        plain_text = plain_text + ALPHABET[index]

        key_index = key_index + 1

        if key_index == len(key):
            key_index = 0

    return plain_text


if __name__ == '__main__':
    # text = 'Cryptography plays a crucial role in safeguarding information within computing systems. It is an integral part of daily life for billions of people worldwide, ensuring the security of both stored and transmitted data. Cryptographic mechanisms underpin essential protocols, particularly Transport Layer Security (TLS), which facilitates robust encryption across numerous applications. However, despite its significance, cryptography is inherently delicate—its security can be entirely compromised by a single design flaw or coding mistake. Conventional software testing approaches, such as unit testing, are inadequate for detecting vulnerabilities in cryptographic systems. Instead, their security is validated through rigorous mathematical analysis and formal proofs, demonstrating adherence to essential security principles. These proofs often depend on reasonable assumptions to substantiate their claims. One of the earliest polyalphabetic encryption techniques is the Vigenère cipher, developed in the 16th century. Unlike simple substitution ciphers, Vigenère encryption employs a repeating keyword to determine letter shifts, making it more resistant to frequency analysis. For centuries, it was considered unbreakable due to its complexity compared to monoalphabetic ciphers. However, it is now easily deciphered using techniques such as the Kasiski examination or frequency analysis of repeating patterns in the ciphertext. Despite its historical importance, the Vigenère cipher no longer provides adequate security, highlighting a key principle in modern cryptography: true protection relies not only on secrecy but also on strong mathematical foundations and computational infeasibility.'
    # cipher = vigenere_encrypt(text, "SRIGALAK")
    # print(cipher)
    c = "UIGVTZGBSGPEPWAIKRKXUNIKDIWRETNCSWMMULRNAEOONQOBERBOOYWSLYQTCZMZMKQTGDYCLVUYIEICSEQTTPGBSCXGREOPVRQRYWIPWWWXBTLVAFVYOQPOGGTKWZRVVNQJEPNCMIQTGEHOKVKARTTIGWJUTSSDGIMJAYDDJRVYMTTDWULGTLCBQGBUGCAZZZKSENHKFZASSFNNWIXONPSCWEBOAWPBGKWIOWSZSIBOCFLKJCGZRLNCHFZZLLYOJJMIUCIDQKTYWSIMZWIIIWIDSKMYRZBEKKMTCCYZLZWTANRYKJVAMPRYMJIVPWIMSKQUNDHYOVDKROECHZBKIESCAXVOFTCKFTMIRJPDGXZGPSYSKZVNECEXLCGJEWIMSKMOTDSOULZOTJCKFSMKNEIBWCGIOXPBGDQYEOBISJQTGWENWJQMNQLKOFZIOOIXYDQYTLKOUFVBEYTSGEIRSZFDORZKTPSDAEOGPARYSTPKSDUMZRAANTTDWJBONRABWZVGDPQESKMLOCDOLVKZIYGFMCVKRLBSDZBOEDIXUIGVTZGBSGPOCDYCLVUYIYSDWRLZHPIBKVKARTTIAJDGLTDKLVLZHCOEYYZOGZRYMJUGTSEWSKQIAWAXSCGYIDAXVWWXMLLZJFWLSOEWGEAZRLTSFXIJHPROFTMZOPSCWEBOAWSOULZOTJPBAEKOPWECLYMYEARYGWAUFEEXVVXKNOOXJVIYOYALDVIYSFMZLZWTSEOCMSAZAYTSSKMZHPIBUCIOMDOXWFNZHPEKJCQKSEPYDPIRPSALWKQIEYCBQGBOOYTOUYVOQFECAJBNEGIQWEZKCTPRWILKVPLYHVLONEHOLYKKNEUBQLVRIVECADXREDULKKQZUEIYFTQVHPRCNZOKNCEOFTZEPEIYFVUVLZYCSIMVELTSFXSKYHOBVKWJEEEBEZVKLPTDWIANIQTCERSONRIDEFZKRPSSKKITTEOPJVYAEYCISEIRYDICXFZIEYTEJZMYIEWKKTWTSTDOJVLANMROSBIHLPDEWKWOTDCYEGTKXTTIUFUVACENLFUUNZAVHYIHEEIMUZXNECSRGNMBECIDAJVUWPACACGJENIZZVZKDFSSFXBKCSNSILMYSFCRSJBNEVACAJSOEIAWAEIZIZNYJWZKQFEXUPITAWYCAJWLRPPOSKQTGAADLVZTSTNDZVKOPSEBLVFZDPSZAKMOTDHSKKWXINAVADXUREAXUVBNEGIQWEZKCTPRWIVULZNQWIXXOGINWJIJEBUKLVAKCFRSLPPOGSLSYYBONRAUWPXXIYCSHCMONXONWIVIRJPDGXZGPSYDJLMVRZTOUKQUNCEVAVATOEOXDPWTSPCBWTGHUEAVKFWTSERYFXUGTSEWSKQIAWFYMELGTTOXKRVJCZMZMKIZIZNKDZVLELSSTZTOTJ"
    print(vigenere_decrypt(c, "SRIGALAK"))