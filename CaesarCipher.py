# we need the alphabet because we convert letters into numerical values
# to be able to use mathematical operations (note we encrypt the spaces as well)
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
KEY = 9


def caesar_encrypt(plain_text):
    # the encrypted message
    cipher_text = ''
    # we make the algorithm case insensitive
    plain_text = plain_text.upper()

    # consider all the letters in the plain_text
    for c in plain_text:
        # check if the character is in the alphabet and is not a space
        if c in ALPHABET and c != ' ':
            # find the numerical representation (index) associated with
            # that character in the alphabet
            index = ALPHABET.find(c)
            # caesar encryption is just a simple shift of characters according
            # to the key use modular arithmetic to transform the values within
            # the range [0,num_of_letters_in_alphabet]
            index = (index + KEY) % len(ALPHABET)
            # keep appending the encrypted character to the cipher_text
            cipher_text = cipher_text + ALPHABET[index]
        # if the character is not in the alphabet or is a space, skip it
        # (do not append it to the cipher_text)

    return cipher_text


def caesar_decrypt(cipher_text):

    plain_text = ''

    for c in cipher_text:
        index = ALPHABET.find(c)
        index = (index - KEY) % len(ALPHABET)
        plain_text = plain_text + ALPHABET[index]

    return plain_text


if __name__ == '__main__':

    # m = 'Cryptography is an indispensable tool for protecting information in computing systems. It is used everywhere by billions of people worldwide on a daily basis, securing both data at rest and data in motion. Cryptographic systems are fundamental to standard protocols, most notably the Transport Layer Security (TLS) protocol, which enables strong encryption across a wide range of applications. Despite its importance, cryptography is inherently fragile. Even the most secure cryptographic system can be rendered completely insecure by a single specification flaw or programming error. Traditional software testing methods, such as unit testing, are insufficient to uncover security vulnerabilities in cryptosystems. Instead, cryptographic security is established through mathematical modeling and rigorous proofs, demonstrating that a system meets the necessary security properties. These arguments often rely on plausible assumptions to validate their claims. One of the earliest and simplest cryptographic techniques is the Caesar cipher, which dates back to around 45 BC. This method encodes plaintext by shifting each letter of the alphabet by a fixed number of positions. While this approach was effective at the time due to the obscurity of the method, it provides no real security today. Since there are only 25 possible shifts, the cipher can be easily broken through brute force. Despite its simplicity, the Caesar cipher remains one of the most widely recognized encryption techniques. However, it offers no real protection, as it can be quickly deciphered by hand. Additionally, its ciphertext is easily identifiable because the frequency distribution of letters mirrors that of the English language. This highlights a key principle in modern cryptography: true security relies not only on secrecy but also on strong mathematical foundations and computational infeasibility.'
    # encrypted = caesar_encrypt(m)
    # print(encrypted)

    c = "LAHYCXPAJYQHRBJWRWMRBYNWBJKUNCXXUOXAYAXCNLCRWPRWOXAVJCRXWRWLXVYDCRWPBHBCNVBRCRBDBNMNENAHFQNANKHKRUURXWBXOYNXYUNFXAUMFRMNXWJMJRUHKJBRBBNLDARWPKXCQMJCJJCANBCJWMMJCJRWVXCRXWLAHYCXPAJYQRLBHBCNVBJANODWMJVNWCJUCXBCJWMJAMYAXCXLXUBVXBCWXCJKUHCQNCAJWBYXACUJHNABNLDARCHCUBYAXCXLXUFQRLQNWJKUNBBCAXWPNWLAHYCRXWJLAXBBJFRMNAJWPNXOJYYURLJCRXWBMNBYRCNRCBRVYXACJWLNLAHYCXPAJYQHRBRWQNANWCUHOAJPRUNNENWCQNVXBCBNLDANLAHYCXPAJYQRLBHBCNVLJWKNANWMNANMLXVYUNCNUHRWBNLDANKHJBRWPUNBYNLRORLJCRXWOUJFXAYAXPAJVVRWPNAAXACAJMRCRXWJUBXOCFJANCNBCRWPVNCQXMBBDLQJBDWRCCNBCRWPJANRWBDOORLRNWCCXDWLXENABNLDARCHEDUWNAJKRURCRNBRWLAHYCXBHBCNVBRWBCNJMLAHYCXPAJYQRLBNLDARCHRBNBCJKURBQNMCQAXDPQVJCQNVJCRLJUVXMNURWPJWMARPXAXDBYAXXOBMNVXWBCAJCRWPCQJCJBHBCNVVNNCBCQNWNLNBBJAHBNLDARCHYAXYNACRNBCQNBNJAPDVNWCBXOCNWANUHXWYUJDBRKUNJBBDVYCRXWBCXEJURMJCNCQNRALUJRVBXWNXOCQNNJAURNBCJWMBRVYUNBCLAHYCXPAJYQRLCNLQWRZDNBRBCQNLJNBJALRYQNAFQRLQMJCNBKJLTCXJAXDWMKLCQRBVNCQXMNWLXMNBYUJRWCNGCKHBQROCRWPNJLQUNCCNAXOCQNJUYQJKNCKHJORGNMWDVKNAXOYXBRCRXWBFQRUNCQRBJYYAXJLQFJBNOONLCRENJCCQNCRVNMDNCXCQNXKBLDARCHXOCQNVNCQXMRCYAXERMNBWXANJUBNLDARCHCXMJHBRWLNCQNANJANXWUHYXBBRKUNBQROCBCQNLRYQNALJWKNNJBRUHKAXTNWCQAXDPQKADCNOXALNMNBYRCNRCBBRVYURLRCHCQNLJNBJALRYQNAANVJRWBXWNXOCQNVXBCFRMNUHANLXPWRINMNWLAHYCRXWCNLQWRZDNBQXFNENARCXOONABWXANJUYAXCNLCRXWJBRCLJWKNZDRLTUHMNLRYQNANMKHQJWMJMMRCRXWJUUHRCBLRYQNACNGCRBNJBRUHRMNWCRORJKUNKNLJDBNCQNOANZDNWLHMRBCARKDCRXWXOUNCCNABVRAAXABCQJCXOCQNNWPURBQUJWPDJPNCQRBQRPQURPQCBJTNHYARWLRYUNRWVXMNAWLAHYCXPAJYQHCADNBNLDARCHANURNBWXCXWUHXWBNLANLHKDCJUBXXWBCAXWPVJCQNVJCRLJUOXDWMJCRXWBJWMLXVYDCJCRXWJURWONJBRKRURCH"
    print(caesar_decrypt(c))
