def trigram_analysis(text):
    # Convert text to uppercase and remove non-alphabetic characters
    text = "".join([char.upper() for char in text if char.isalpha()])

    # Dictionary to store trigram frequencies and positions
    trigram_frequencies = {}

    # Iterate through the text to extract trigrams
    for i in range(len(text) - 2):
        trigram = text[i : i + 3]
        if trigram not in trigram_frequencies:
            trigram_frequencies[trigram] = {"count": 0, "positions": []}
        trigram_frequencies[trigram]["count"] += 1
        trigram_frequencies[trigram]["positions"].append(i)

    return trigram_frequencies


if __name__ == "__main__":
    # Example usage
    sample_text = "UIGVTZGBSGPEPWAIKRKXUNIKDIWRETNCSWMMULRNAEOONQOBERBOOYWSLYQTCZMZMKQTGDYCLVUYIEICSEQTTPGBSCXGREOPVRQRYWIPWWWXBTLVAFVYOQPOGGTKWZRVVNQJEPNCMIQTGEHOKVKARTTIGWJUTSSDGIMJAYDDJRVYMTTDWULGTLCBQGBUGCAZZZKSENHKFZASSFNNWIXONPSCWEBOAWPBGKWIOWSZSIBOCFLKJCGZRLNCHFZZLLYOJJMIUCIDQKTYWSIMZWIIIWIDSKMYRZBEKKMTCCYZLZWTANRYKJVAMPRYMJIVPWIMSKQUNDHYOVDKROECHZBKIESCAXVOFTCKFTMIRJPDGXZGPSYSKZVNECEXLCGJEWIMSKMOTDSOULZOTJCKFSMKNEIBWCGIOXPBGDQYEOBISJQTGWENWJQMNQLKOFZIOOIXYDQYTLKOUFVBEYTSGEIRSZFDORZKTPSDAEOGPARYSTPKSDUMZRAANTTDWJBONRABWZVGDPQESKMLOCDOLVKZIYGFMCVKRLBSDZBOEDIXUIGVTZGBSGPOCDYCLVUYIYSDWRLZHPIBKVKARTTIAJDGLTDKLVLZHCOEYYZOGZRYMJUGTSEWSKQIAWAXSCGYIDAXVWWXMLLZJFWLSOEWGEAZRLTSFXIJHPROFTMZOPSCWEBOAWSOULZOTJPBAEKOPWECLYMYEARYGWAUFEEXVVXKNOOXJVIYOYALDVIYSFMZLZWTSEOCMSAZAYTSSKMZHPIBUCIOMDOXWFNZHPEKJCQKSEPYDPIRPSALWKQIEYCBQGBOOYTOUYVOQFECAJBNEGIQWEZKCTPRWILKVPLYHVLONEHOLYKKNEUBQLVRIVECADXREDULKKQZUEIYFTQVHPRCNZOKNCEOFTZEPEIYFVUVLZYCSIMVELTSFXSKYHOBVKWJEEEBEZVKLPTDWIANIQTCERSONRIDEFZKRPSSKKITTEOPJVYAEYCISEIRYDICXFZIEYTEJZMYIEWKKTWTSTDOJVLANMROSBIHLPDEWKWOTDCYEGTKXTTIUFUVACENLFUUNZAVHYIHEEIMUZXNECSRGNMBECIDAJVUWPACACGJENIZZVZKDFSSFXBKCSNSILMYSFCRSJBNEVACAJSOEIAWAEIZIZNYJWZKQFEXUPITAWYCAJWLRPPOSKQTGAADLVZTSTNDZVKOPSEBLVFZDPSZAKMOTDHSKKWXINAVADXUREAXUVBNEGIQWEZKCTPRWIVULZNQWIXXOGINWJIJEBUKLVAKCFRSLPPOGSLSYYBONRAUWPXXIYCSHCMONXONWIVIRJPDGXZGPSYDJLMVRZTOUKQUNCEVAVATOEOXDPWTSPCBWTGHUEAVKFWTSERYFXUGTSEWSKQIAWFYMELGTTOXKRVJCZMZMKIZIZNKDZVLELSSTZTOTJ"
    trigram_freq = trigram_analysis(sample_text)

    # Sort trigram frequencies by count in descending order
    sorted_trigram_freq = dict(
        sorted(trigram_freq.items(), key=lambda item: item[1]["count"], reverse=True)
    )

    print("Trigram Frequencies with Positions:")
    for trigram, data in sorted_trigram_freq.items():
        print(f"{trigram}: Count = {data['count']}, Positions = {data['positions']}")
