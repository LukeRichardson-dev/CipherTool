def apply(text, substitutions):

    new_text = ''

    for idx, character in enumerate(text):

        sub = substitutions.get(character)

        if sub is not None:

            new_text += sub
        else:

            new_text += character

    return new_text

def count(text, characters):

    frequencies = {
        i: 0 for i in characters
    }

    for character in text:

        if character in characters:

            frequencies[character] += 1

    return frequencies
        


EXAMPLE = """GHDU E

BRX FDQ DGG WKLV WR BRXU SLOH RI \"MXVW LQ FDVH\" OHWWHUV. LI BRX JHW WR UHDG LW WKHQ L VXVSHFW LW ZLOO UDLVH PRUH TXHVWLRQV WKDQ LW DQVZHUV DQG KRSHIXOOB L ZLOO EH DURXQG WR DQVZHU WKHP.

LI HYHUBWKLQJ JRHV DFFRUGLQJ WR SODQ BRX ZRQ'W HYHQ RSHQ WKLV, DQG WKDW ZRXOG EH EHWWHU IRU XV DOO, HVSHFLDOOB IRU MRGLH.

L DP ZULWLQJ WKLV VR LW FDQ EH XVHG DV HYLGHQFH LQ WKH KRSH LW ZRQ'W FRPH WR WKDW. DW WKH HQG RI WKH OLJKWKRXVH FRQVSLUDFB LQYHVWLJDWLRQ L WROG BRX WKDW MRGLH KDG UHTXHVWHG HAWHQGHG OHDYH DIWHU D KDUG FDVH, EXW WKDW ZDV QRW WUXH. VKH GLVDSSHDUHG OHDYLQJ PH D QRWH VXJJHVWLQJ WKDW VKH KDG MRLQHG WKH FRQVSLUDFB. L KDYH OHIW PB QRWHV IURP WKH HQG RI WKH LQYHVWLJDWLRQ LQ WKH FDVH ILOHV LQ FDVH WKHB KHOS.

ZKHQ L UHDOLVHG WKDW VKH ZDVQ'W FRPLQJ EDFN L WUDFNHG KHU WR GHOKL ZKHUH L IRXQG D WURYH RI SDSHUV HASODLQLQJ PRUH DERXW WKH JURXS, DQG WKDW UHOLHYHG VRPH RI PB DQALHWB, EXW QRW DOO. D URJXH DJHQW LV QHYHU D JRRG WKLQJ ZKDWHYHU WKHLU PRWLYDWLRQ.

L DVNHG D IHZ IULHQGV WR NHHS DQ HBH RXW IRU MRGLH DQG DW ODVW L WKLQN L PDB KDYH SLFNHG XS KHU WUDLO. D FROOHDJXH LQ WKH XV LQWHUFHSWHG WKH DWWDFKHG OHWWHU ZKLFK L DP SUHWWB VXUH ZDV DGGUHVVHG WR KHU. PV FLIUDU LV MXVW WKH VRUW RI DOLEL VKH ZRXOG XVH DQG WKLV LV WKH VRUW RI FDVH L FDQ LPDJLQH KHU ZRUNLQJ RQ.

L ZLOO KHDG RYHU WR WKH XV WR VHH LI L FDQ WUDFN KHU GRZQ. LI L DP VXFFHVVIXO DQG FDQ SHUVXDGH KHU WR UHWXUQ, WKHQ BRX ZRQ'W JHW WR UHDG WKLV MRXUQDO. LI L IDLO WKHQ L JXHVV ZH KDYH VRPH GLIILFXOW FRQYHUVDWLRQV DKHDG.

YHUB EHVW ZLVKHV,

KDUUB"""

EXAMPLE_2 = """YFDS JZ RHMSDS,
H DJ BSHGHQT GX PXN HQ JP RDEDRHGP DZ RADHS XM GAF UHSTHQHD KDQVHQT DZZXRHDGHXQ HQ GAF AXEF GADG PXN BHCC KF DKCF GX DZZHZG HQ D YFCHRDGF JDGGFS. XQF XM XNS JFJKFSZ MHQYZ HGZFCM HQ GAF FIGSDXSYHQDSP EXZHGHXQ XM EXZZHKCP ADUHQT KFFQ SXKKFY, BAHCF QXG VQXBHQT BADG ADZ KFFQ ZGXCFQ XS GX BAXJ GAF HGFJZ KFCXQTFY.
H DJ DMSDHY GADG GAHZ BHCC ZFFJ ZX AXEFCFZZCP NQZEFRHMHR GADG PXN BHCC KF SFCNRGDQG GX HQUXCUF PXNSZFCM BHGA XNS RDZF, AXBFUFS PXN DSF XNS KFZG AXEF. EFSADEZ HM H FIECDHQ GAF NQNZNDC RHSRNJZGDQRFZ HQ BAHRA BF MHQY XNSZFCUFZ GAFQ GAF JPZGFSP BHCC KF FQXNTA GX FQGHRF PXN. HM HG HZ QXG, H RDQ DZZNSF PXN GADG BF DSF ESFEDSFY GX EDP BFCC MXS PXNS GHJF, FIEFSGHZF, DQY FMMXSG.
XQ GAF JXSQHQT XM GNFZYDP GBFQGP-MHSZG ONQF GAF RAHFM GFCCFS XEFQFY GAF ESFJHZFZ DQY RXQYNRGFY AFS NZNDC HQZEFRGHXQ. FUFSPGAHQT BDZ HQ XSYFS BHGA XQF DCDSJHQT FIRFEGHXQ: GAF YXXS GX GAF JDHQ UDNCG BDZ XEFQ DQY D KXI BDZ CPHQT XQ GAF MCXXS. BAHCF HG ZFFJFY FIGSFJFCP NQCHVFCP GADG GAF ZDMF ADY KFFQ CFMG HQ GAHZ ZGDGF ZHQRF MSHYDP DMGFSQXXQ, GAF CDRV XM DQP ZHTQ XM D KSFDV-HQ, XS DQP YHZGNSKDQRF GX GAF XGAFS RXQGFQGZ XM GAF ZDMF, CFY AFS GX GAF RXQRCNZHXQ GADG GAF RCFDQHQT XS ZFRNSHGP ZGDMM ADY MDHCFY GX ZFRNSF GAF UDNCG BAFQ RCXZHQT MXS GAF BFFVFQY. DCC GAF ZGDMM BFSF DYDJDQG GADG GAHZ RXNCY QXG KF GAF RDZF DQY BAHCF BF RDQQXG SNCF XNG GAF EXZZHKHCHGP XM D RXQZEHSDRP, BF ADUF KFFQ NQDKCF GX FZGDKCHZA DQP FUHYFQRF MXS GADG.
MNSGAFS DYYHQT GX XNS RXQMNZHXQ, BF ADUF KFFQ NQDKCF GX FZGDKCHZA GAF ESXUFQDQRF XM GAF KXI HGZFCM. HG BDZ SFJXUFY MSXJ ZDMFGP YFEXZHG GBFQGP-GASFF, KNG GADG CFYTFS FQGSP ADZ QXG KFFQ NEYDGFY HQ XUFS GBX ANQYSFY PFDSZ. DZ BHGA XNS XGAFS KXIFZ GAF RXQGFQGZ DSF ESHUDGF GX GAF XBQFSZ, ZX BF ADUF QX VQXBCFYTF XM BADG HG JHTAG ADUF RXQGDHQFY, HM DQPGAHQT.
THUFQ GAF RHSRNJZGDQRFZ GAF KDQV HZ SFCNRGDQG GX HQUXCUF GAF EXCHRF. HM QXGAHQT ADZ KFFQ ZGXCFQ, GAFQ HG HZ YHMMHRNCG GX ZFF BADG RSHJF RXNCY KF SFEXSGFY DQY GAF HQUFZGHTDGHXQ HGZFCM RXNCY ZFUFSFCP YDJDTF GSNZG HQ GAF KDQV. KP DZZXRHDGHXQ, GAHZ RXNCY DCZX ADSJ GAF HQGFSFZGZ XM XGAFS JFJKFSZ XM GAF UKD.
H DJ GXCY GADG PXN DSF XQF XM GAF JXZG DRRXJECHZAFY HQUFZGHTDGXSZ HQ JDGGFSZ XM GAHZ VHQY, DQY GADG PXNS RXJECFGF YHZRSFGHXQ RDQ KF DZZNJFY. H DJ GAFSFMXSF BSHGHQT GX DZV HM PXN BXNCY KF BHCCHQT GX GDVF GAHZ XQ MXS NZ. HM PXN RDQ DZZNSF NZ GADG QX ADSJ ADZ KFMDCCFQ GAF KDQV, GAFQ BF BHCC RCXZF GAF RDZF DQY SFZG FDZP. HM PXN RDQ MHQY FUHYFQRF XM MXNC ECDP KNG DSF NQDKCF GX RXQRCNYF GAF HQUFZGHTDGHXQ, GAFQ BF BHCC HQUHGF GAF CXRDC XS MFYFSDC DNGAXSHGHFZ GX GDVF XUFS. HM PXN DSF BHCCHQT DQY DKCF GX ZXCUF GAF JPZGFSP MXS NZ GAFQ, HQ DYYHGHXQ GX PXNS NZNDC MFF, BF BHCC KF DKCF GX XMMFS D ZHTQHMHRDQG KXQNZ. BF AXEF PXN BHCC DTSFF GX DG CFDZG YHZRNZZ GAF RDZF BHGA NZ.
PXNSZ ZHQRFSFCP,
CPQQ MSDQV."""

ALPHABET = ''.join(chr(65 + i) for i in range(26))

def test():
    alphabet = ''.join(chr(65 + i) for i in range(26))
    print(alphabet)
    
    subs = {
        "G": "t",
        "X": "o",
        "A": "h",
        "F": "e",
        "C": "l",
        "Y": "d",
        "D": "a",
        "S": "r",
        "H": "i",
        "R": "c",
        "Q": "n",
        "J": "m",
        "K": "b",
        "Z": "s",
        "M": "f",
        "T": "g",
        "B": "w",
        "U": "v",
        "P": "y",
        "N": "u",
        "E": "p",
        "V": "k",
    }

    # subs = {
    #     alphabet[i]: alphabet[25 - i]
    #         for i in range(26)
    # }

    freqs = count(EXAMPLE_2, ALPHABET)

    items = list(freqs.items())
    items.sort(key=lambda i: i[1], reverse=True)

    for i in items:
        print(i)

    print(apply(EXAMPLE_2[:], subs))


