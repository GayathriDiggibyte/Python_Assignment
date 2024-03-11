import unittest

from src.Assignment4.util import merge_the_tools
class MyTestCase(unittest.TestCase):
    def test_something(self):
        merge_the_tools(
            "NFFFGVTLLMWEEKUIGNUCDSRPHPNFAKEORKVXFPJTBHZHTTSZIMDLGWCNLQSMCXCUHXROMAJPJIXCEPBMBEAHACXMSPAXMCRVZIMOLVDUEAXKPAWSFYCHBBVVQVSFZJAZUMNFKQZQTYAKZWFEXHNYIJVAEQFEBIFVWUAGMCWFAWQBVVHSEVSOEPQKFWQHGVCEPFLCJJJLIZNFWUZCPTQTIHGOFWXNSBRJIENRQXDYYQFXMEZCXSXFBDVIAUVUWOFGTVYJUDJSVORHURJRJJYMMWUOQRKOFQVANVLHYWZVKRCEKOXVXWHLUDAKUMBBEYERTPYTMAOYRSFDGCYDAHPUKRFGDIJIGNZZFYURYKRRCWWJZUOBDDWPWDVALEKRUJSZJOSJYJCAIYLJUAKXFGMCLJEWQOPKXJJJXBSXMVYUVJDQJQPPWETKNXGDLYPKJYVHBOEQLEKIQQYZIQQEULOJIXPTXEGGFBPGRUYEALNQBNSJDKPZWGJEFYACEIIJJASDUQHWBWNEKHPPRHPNPAUUYWYEEIONIIQEAABCWQIGXYYQFNEUNAQNWQTAYHPHRINSIQUEGENFCLWJACFPCXCYNVYMFPVYXKQFBMMHRZNVMLFMNMBPKFPXCPLJEIICTYHUNTDEUSZGDGUQVXHFCWEHLSQQAYSVZBRMVVSPPTYTASLXSVCURIBFAUVBSPYTQQFNLXFATFVVXJSREUMVEPAFJXIEOGXHWFWJEBMXGJSGSKXWGLULBUQMUASKISTFXQQDREBYOVGGGDDOPXZSTRGPTZCCRVHQLZTFEUDUQLAYQFMHEOBAHIRBHTDARMQCLLHRGMLYZOYQTMXAAZCIHTJQPMSGYKKLVUDDGQDIEBYAOXAQWEYFXJXMVRUVBFHXBMCJCGRJHPJXNLOLPOTOYQDVIXTLEAKFONPSTIBCYKCNXQYMERBEKGAUDTFKVQRLFIDYRFCRREEPWEDDYGHIMJCSCHEZZVKEEQEXXJOOPUFMYLPWTYEGIIAMSEORZAYFQEENNSEDMLRNYIJSGQAQYCFSGVKHVKPOOTBEMHJAVANTKZNSPNJPPQIXLUFGGUUWPYADHJECLTYVSLQJBZBQRJQCFVKLRHHGHKKOVQTHJREEEUPFVQYMZOQGLBRCKBKRLWFIMARYRWEYSTDQKDELRVSCYLGIORZBPGKCHBCAZGASBEKLHOZBLRFJEMTTFUWUDGYKIAMHINBMTLZCCYDNRJZYXSRCPNWSWXCEZQNKFRWYEVDGWGWNRVLQPESEURWQQAWPTLZYCVZHTCPPKLEEIQUYUPCQIBIYDENWQNVUKUDDWTUGGZKPPHNLWREEUMCYRPUJEPFPLJUHCRQKQCZHJOUHIYLCLPCEFXPLOUCCFZLJQBUGGVPRKJZUKKYVABBHASSQOXSUWEDMHZUNVJFFSEZCQXZQACZAWURLRJHNPKBXMVMHEROWXPBOOCGPFIPBCIOVUVKJILGUGVBKMRIMGLCUOKJVSBYWLNRFKBRSOZOUURGJIPVOCZJQJUNEXMCJBUQLXHEMHUIBMPKUGHJIGUBSOOWMCYXDUNPUVVICPQFBHSYNZHYGBZYRPWFUWCXRSONNLVRDNYEVQEIQLGYOHYGZUNTSQSJIHWXSTQVHOCCFGMXUVVKCVSDRGYJWRVGYRFSNVQULUYQCKPYFKJKFBNYHMIFFDNDWSXJPPFBLDTOOJOTTXFBBTZKHHQMMFRJYQUPGAQTDKJRTYNOVSRYNRJWABKPGBYGUSWCSOVYYFPTDEKAZBZOUKLXLXMRZKATEWXXMSXNXMGCTSFUUEIOQVLBTZUUJUPQSMPFEMSEAAITTNPNTYDJVRKQQFMCZBSSPHZWTRCTRKPMYEZTEFDCYNSOUHSWKMQATPYOIAKBMBOMFPGMUJOUYILVPDRAQJALYACGAOHOPXBWNJIJSWESFPNUSGUKPWYPYCXAQFPFCQBRBKBTIFNNUDKOLGBBFZSDBQERXTYBLBTMLUHWZWJVZVJLCMOHLGMOWQHTLFVYHQMUKVQLSCGTXREBEUKRBXGZPNVBVQBEIOASJRDBVLVUEBWKYGCBFKAXZVYUNBAVPBPBUUCPFZLMDHWBQYCXKEUKCUGPWHNNKCOEZTVGSGSXQPAIPEFAJAKLUQCSZRGJWUPVNMBIVUHLLITCMACXAOKXHPPGGXSESJZFWDPTZXEKFZMTBRTCFFBMUSVDQPHIYJPWMFPLCVXJWJEYAXCIDDUZXRCNGMXFXPDJUTWYOTJLENLHNNPSSLRPDWFLKCSHTWQPRONHJYUNOFWDSLVKZOAEKFPUJKBDGTSZJIGSIBIWGEBBSWLRNNVZUMUEWXJETDDENMXWNFUVLWWDSIUHVRHSEDWACHHVKKAYWZWLGQHRMFVHNROLJVDNYBPDKWYUHAUFBQTHJAZVFWEVNVIWSNLTQBWAXWWGXTOALHIUJJSQFYNSTVRMKCFCFBCDXBLWUZXHIHCRQWKVUXPQVGCFLJKQMOVLPJILIHTTQXMGVWBRUSHPBLWMUIEGXAUMJCATLVMBUBJPXMIREQIFDHRYPYGMYABJEBERYTUSUDJRPRLUJTBNCVNUTTGTWJCCMIUKBOEVSNNJHYFSTHFYCSSXOAQMMUOYCILEZPZTFOCOOIGIRMGVGASWAKIMEXNIHYMGPOZUCEKRORBFFJCLJWKLGSAMPPUXPJFEXFBBJLUXCVEHGIVREFFKZHWPWSOLBTRAASCJEYIIWOQCWNUAUBMTIKKGDATEWKFWDJIHHSPDJHGFWCISFWMNHYTKBMOXYVTBEDKOWARFJZMGDWYITMXANSKOGANFWIGCMRQITIPCJDKNALXTZVTMPFCWFPBBYJEMCWWVGLAQOMFQZEJZBENRJQPPHQSFBYREVPBBADTRQAHPFTQGXEZJUOADEULITCOQURTUVNNNPXEUQXBPBAAXRAAVVLFQQTIKNBGIQUXGRDCJAFABIBYZDBWAMCQEXAOKCXUURTCKXFTXKTBSWBRACQARSTXRTOEXLASCUUMRZHQMCTEBXYBBODSIWSZSGFPRGHTAEHTFQLRUFYVCYWDOCYWYQXSYFIPLRKLVTGDJRUDYUBCSZIIBIGCAGUYLCPWWZJTSRWDITGJNJNIJXQKHXMHFJHQNWMJVXDPOZSYSBJIKZQTWIEEHSNMBVERRQAPPFEFHXEBYPJKOBELMKRTEEIGZMZTFZKUFOAONGPNVZYKCEXOOOISUQAWEZPJBZGIPIWFOLULMSXPYWDMMNHHDJDKLUTMTZUKHSRXDMJQGIHFFKTRYCYDMDNXXJJSIFDSXWPCIAUPLBWQOPHOUIRGLHDJQOBAVGSUFKWNMTEXWCNKUXAOFSUSZZBRNFRKNMESYCIKVMKURZGLWHZDBTWCSZTHGKRUYVOWZWJXLTRCSZNRGOUHHSJBSEIYRBUPYLMXJVUWQNAINPZVDWDKOONGTXHKYDBWONWYKSUAIVLVMMQQIVAXMOFFLMRMSSKGIIGUBDXJAIGMWYCFUFCGVJNIYGUQYHYIPFFQKCBKMHWIIBNCGRKDBZLZFIRFPPQEUVXGXAQLKPTSSJWACGDDHQEMYXTPNJWJETQDVGOFXKXPTTPVBUBILHWJFSBSBXBISTLNCATZKSRFMGCPBDAOLYXQQAKSXNAPHNFJPYKBSBGEKJWNMWBZUARLBBFAPHQWWXHMVRNNVUUFFQSTOVTKVKXYOCZDLPBIMKUJDHYYDUDIMXCCSXNQJKOXPNAAEDKSNGDRQERTYXENUIPPHCHQPVOELQGRWRKJZNCPTULSTRHNZWEIBNYQJOWWFCNBVZMVNRKINVCGOJVNICVLPWBAKZYRBMUXLJSACEJPCLXQXUGFWDQOZTOMSNDTBYSMJMPLRYATLZLITRNSVFGUYUISJMOKMGZVVOGMOIHZHSIAMXUHFADFXMYGAMTMUUHRKPFYXMZGHJITJDCODFTARRJRFEFCAOTKDBICNJIWTRRCUTSZZLCSFLMMRTORIKBLLLQAWYZPRQTLKNNLZPFGCTSTNJKVVNIGAYIWZHOQAJEMXRXYGEEIYWBLHNICCQKCRTAQCOIEYMQXDNVJSZTSXWDFLLJNDURWPSOTIXYIJOFPEAAYBUQBQVIEIRRNNLKCFAYNXWWJMDASEASHUIINFSRNKKDXXPCCPCSPAOAMRAHXAZHXKRMPKFFUPKTPZXRQZJFZZFOTFXSIWZFGRRYBWFXNPSCQQWGRHOTJTHCBEWLCYQLRJLSHSRUHLZZBXFVETOPPXTSDQDHOVSFGDZNVSJEDIFHHNCOISDZRXRUNWBDRWKXBJMZDWFGGLNOYRCGJFGCCZWRWAUPWEPXPBYSXEZGPOUPIYXTDFWIFSZDUWUQCJQSNQMMULSLCOAKMADSFZCMUDROZMHCXZWKPIXMWRXYGAKSAPMHROWLSNBRBKVZJRLBCKNYCMYIMKCOZPYQDUDVJHPNRMMDGZGIKVIOHGWWQAMRPKIVGNSSUJFOWTTCSZMEUUSDCQZURMLGYVDFJWZFFEVBZOFRPTYLPQPTJONACZIBWMIFIJNPNKTMZAFQUFCLYTFHJUHMTRPQDZXNIMFXXYLYYQOUYSIWLPDVJMJDFAVJZUYHHFEGDPEEHUAHNKDAZIXJWGOCGLNFFNOOTUUWLYCTVFAIPGIPOIYNOMPXXCEEPTTINPHZQJULQWVGEFVTNVGCJXZIZFMQYHBOXIPNTLYKJTSOYNJOIRQTORBPWNFXVINUSEHMPHYYCSOCFXQPOIICBJTYYZXTJMPCQWQFFQFJIWMNTEEKNMMOXGOVHNRSZGUPFKWMAEWIAKXVQBFFPUWOCKMLADDBLYRSIPFLVDVXPTTFWYLMUHCWTOHTRLVFLOXTFEGBHCYWVRETSPHMWKJRYSNSDIZQYWKDDSGMUFJRYNLQESFCCQTDIGVOQWEOSQUXLAKFHVZGIMYOEDQJVJOEQLUGHAXBRRZCTJJBEIJOWHCDLSMGDCMTNICUJBXASWENFPQJAZZWHBZUVNCZPPUEXYAGZYITUOHCEXNEZNCGQCAMPENHTHLTIMBHMMBGCIIGHWMGLPOBTQNKVCRQMFLUTPBFBCNDMWMWUACFRTGKJWXEYQXMVIGQXKVAOLGBHSXBUBIMUOYGMVMNMJZJUICRUZSIKAJRUIUOMECIVBQHYDUMMWYGGAAAZUIKUUDOEAESEHBZKRJIWFXJBVRJVTJWNUGJOMZSMENSNOUXHDHEIEPMZIXWCHTRBBDRNCLBIYWVMQUWVCADIRRKZPGDYBXZDASSCDWLCSIQIDMFHOKPHCZHTIMRJJSOJKHMPDZRVJKFMWKVNULUYMDTWQMGBEWLQDZGIAZDJJKWIWRVTERTTVNPNZXOGUBWZAEIAGNKPAIXWBURGMLBJYQYZQOFMQELSKTVQHFGHPFFQAXYOIZZIQXHINPUFTFYDBTWIAERRJYHLVGZFFYNXXXFNMBSHJSMKNIUPMNGYLOJHUJOBJEZJBGWPKQYTJMDWXZMLMSJXITGEEVGNZHYCPUTZNTSWFXUCWIOIDXILSOQWLYMMFKQUHJUUEOSKMOOKXCVACFNUTFTHDFTIRMFAXZWCPOODDCQCFLEJQRFLXYUAFQLXCQZZRWBGKPKPUCRBNVKFPPSMQNOVDZUFPUGGQKPCBBSVDLWSJIXYYPMOEALHAGORCXASHRUKSOGVCEPLNMJNDVBIXORZUGRWFTQMKNYCBEZFLOQYCBNFYONWEHVZNOXSJOGTDEXELWMWMCWQGJWEZLCDSAEHQCBASHTVORBZPNXESVUYGSEFEJKYJP",
            5784)
        self.assertEqual(
            "NFGVTLMWEKUICDSRPHAOXJBZQY",
            "NFGVTLMWEKUICDSRPHAOXJBZQY")


if __name__ == '__main__':
    unittest.main()
