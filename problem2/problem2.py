import decision_tree as dt
import scan
import utils

# P = [('m', 58614), ('make', 58625), ('tried', 60077), ('well', 61320), ('find', 63153), ('dog', 63341), ('time', 68191), ('little', 69421), ('also', 70045), ('use', 70294), ('price', 70352), ('much', 70683), ('ve', 71991), ('really', 80878), ('would', 82506), ('get', 84809), ('amazon', 85218), ('best', 101359), ('food', 108271), ('flavor', 120831), ('tea', 130919), ('taste', 132704), ('product', 133129), ('one', 138624), ('love', 138818), ('coffee', 147426), ('like', 193545), ('good', 202799), ('great', 219086), ('br', 475248)]
# N = [('eat', 17200), ('also', 17232), ('tried', 17610), ('water', 18047), ('box', 18086), ('little', 18467), ('first', 18497), ('bad', 18866), ('time', 18944), ('m', 20195), ('dog', 20209), ('better', 20336), ('great', 21201), ('even', 22504), ('buy', 23674), ('amazon', 24145), ('really', 25864), ('much', 26233), ('get', 26882), ('tea', 29429), ('food', 33558), ('flavor', 40917), ('would', 43334), ('one', 44099), ('coffee', 44551), ('good', 49750), ('product', 54725), ('taste', 58095), ('like', 76097), ('br', 171874)]

P = [('espresso', 7391), ('weeks', 7412), ('iced', 7467), ('recently', 7477), ('coffees', 7511), ('says', 7588), ('special', 7588), ('plain', 7612), ('bowl', 7614), ('plastic', 7620), ('single', 7669), ('body', 7671), ('20', 7682), ('run', 7721), ('flour', 7724), ('giving', 7731), ('yes', 7754), ('friend', 7756), ('aroma', 7804), ('version', 7843), ('mild', 7844), ('delivery', 7863), ('smaller', 7880), ('vet', 7880), ('container', 7881), ('heat', 7887), ('machine', 7897), ('brown', 7946), ('course', 7958), ('hand', 7994), ('place', 7998), ('drinks', 8026), ('line', 8048), ('end', 8057), ('daily', 8082), ('surprised', 8086), ('recipe', 8087), ('believe', 8103), ('pet', 8103), ('overall', 8111), ('helps', 8121), ('service', 8122), ('simply', 8125), ('subscribe', 8128), ('finally', 8170), ('cocoa', 8192), ('blue', 8210), ('cook', 8215), ('caffeine', 8227), ('wife', 8231), ('slightly', 8244), ('feed', 8244), ('exactly', 8247), ('almonds', 8251), ('chip', 8274), ('chew', 8279), ('rather', 8289), ('salty', 8299), ('soy', 8308), ('cut', 8315), ('french', 8319), ('wasn', 8349), ('crackers', 8355), ('jerky', 8392), ('second', 8400), ('couldn', 8410), ('part', 8421), ('lemon', 8435), ('convenient', 8436), ('flavorful', 8488), ('clean', 8558), ('online', 8559), ('start', 8593), ('enjoyed', 8608), ('grain', 8658), ('mixed', 8670), ('cans', 8703), ('easily', 8732), ('night', 8749), ('spice', 8760), ('picky', 8782), ('tell', 8831), ('haven', 8865), ('choice', 8925), ('maybe', 8938), ('read', 8945), ('hair', 8952), ('100', 8962), ('often', 8969), ('type', 9012), ('daughter', 9040), ('gets', 9092), ('decaf', 9102), ('mouth', 9109), ('problems', 9115), ('brew', 9125), ('pieces', 9135), ('canned', 9207), ('dried', 9212), ('nuts', 9231), ('oatmeal', 9238), ('pleased', 9264), ('teeth', 9273), ('beef', 9330), ('cooking', 9333), ('took', 9341), ('goes', 9373), ('starbucks', 9422), ('snacks', 9512), ('side', 9525), ('difference', 9543), ('fiber', 9606), ('wanted', 9613), ('ginger', 9716), ('market', 9728), ('else', 9755), ('alternative', 9756), ('thanks', 9773), ('cinnamon', 9787), ('fan', 9802), ('potato', 9891), ('money', 9972), ('anyone', 10018), ('week', 10021), ('ice', 10065), ('friends', 10074), ('gave', 10136), ('life', 10164), ('wheat', 10209), ('sometimes', 10220), ('either', 10251), ('cold', 10294), ('etc', 10309), ('son', 10389), ('yum', 10399), ('open', 10444), ('fantastic', 10477), ('everyone', 10542), ('thank', 10569), ('meat', 10644), ('likes', 10709), ('boxes', 10726), ('ordering', 10738), ('although', 10759), ('crunchy', 10764), ('juice', 10891), ('seem', 10923), ('everything', 10938), ('powder', 10962), ('gift', 10973), ('soup', 11029), ('serving', 11044), ('help', 11045), ('let', 11055), ('month', 11148), ('went', 11149), ('longer', 11158), ('weight', 11183), ('super', 11191), ('fine', 11224), ('item', 11231), ('syrup', 11268), ('keurig', 11277), ('nothing', 11285), ('cost', 11287), ('pasta', 11376), ('white', 11378), ('ago', 11378), ('ounce', 11431), ('cookie', 11436), ('red', 11463), ('soft', 11469), ('must', 11486), ('least', 11487), ('glad', 11497), ('reviews', 11512), ('minutes', 11565), ('packaging', 11601), ('decided', 11629), ('spicy', 11646), ('couple', 11668), ('fact', 11673), ('next', 11699), ('plus', 11723), ('received', 11729), ('instead', 11734), ('liked', 11932), ('quickly', 11941), ('corn', 11964), ('yet', 11983), ('others', 11987), ('prefer', 11997), ('look', 12024), ('roast', 12036), ('stars', 12039), ('started', 12199), ('8', 12202), ('bitter', 12218), ('quick', 12240), ('isn', 12269), ('wish', 12295), ('company', 12330), ('cheaper', 12358), ('oz', 12455), ('times', 12497), ('ones', 12521), ('won', 12527), ('href', 12531), ('value', 12576), ('away', 12604), ('gp', 12627), ('bold', 12673), ('baby', 12812), ('house', 12819), ('arrived', 12839), ('http', 12842), ('12', 12893), ('three', 12899), ('might', 12908), ('www', 12915), ('save', 12922), ('bread', 13072), ('fast', 13075), ('meal', 13213), ('cream', 13252), ('review', 13455), ('cheese', 13469), ('teas', 13511), ('beans', 13531), ('problem', 13540), ('case', 13570), ('rich', 13641), ('variety', 13800), ('extra', 13878), ('drinking', 13879), ('large', 13935), ('top', 13948), ('honey', 14053), ('energy', 14101), ('said', 14112), ('able', 14147), ('10', 14209), ('probably', 14287), ('absolutely', 14385), ('husband', 14468), ('making', 14497), ('comes', 14635), ('seems', 14654), ('especially', 14665), ('recommended', 14666), ('popcorn', 14680), ('breakfast', 14706), ('smell', 14752), ('bottle', 14767), ('available', 14877), ('days', 15040), ('deal', 15082), ('tasted', 15131), ('kind', 15243), ('months', 15249), ('black', 15358), ('awesome', 15398), ('us', 15522), ('flavored', 15541), ('peanut', 15542), ('come', 15672), ('added', 15699), ('works', 15699), ('came', 15718), ('trying', 15819), ('purchased', 15838), ('smooth', 15857), ('light', 15860), ('several', 15874), ('things', 15895), ('thought', 15908), ('usually', 16000), ('kids', 16022), ('getting', 16222), ('health', 16277), ('amazing', 16277), ('half', 16455), ('amount', 16494), ('bar', 16618), ('may', 16654), ('candy', 16778), ('brands', 17205), ('anything', 17257), ('vanilla', 17325), ('fruit', 17329), ('cereal', 17430), ('grocery', 17487), ('blend', 17509), ('home', 17566), ('texture', 17647), ('purchase', 17688), ('package', 17963), ('almost', 17985), ('full', 18013), ('loved', 18061), ('family', 18077), ('dry', 18120), ('per', 18283), ('going', 18358), ('bad', 18432), ('6', 18444), ('expensive', 18511), ('coconut', 18727), ('dark', 18798), ('com', 18827), ('worth', 18869), ('rice', 19066), ('another', 19141), ('morning', 19151), ('feel', 19207), ('around', 19215), ('people', 19329), ('last', 19723), ('stores', 19776), ('real', 19889), ('looking', 20002), ('quite', 20089), ('year', 20127), ('bars', 20292), ('protein', 20298), ('actually', 20305), ('yummy', 20309), ('fat', 20331), ('foods', 20443), ('new', 20579), ('see', 20783), ('diet', 20890), ('shipping', 20963), ('d', 21058), ('calories', 21108), ('however', 21272), ('didn', 21325), ('big', 21628), ('take', 21795), ('low', 21828), ('buying', 21871), ('work', 21973), ('butter', 21998), ('ordered', 22149), ('cups', 22200), ('local', 22316), ('sauce', 22352), ('tasting', 22356), ('thing', 22442), ('gluten', 22515), ('bags', 22538), ('sure', 22737), ('pretty', 22861), ('chicken', 22910), ('though', 23061), ('size', 23138), ('products', 23183), ('regular', 23501), ('highly', 23572), ('back', 23778), ('put', 23844), ('hard', 23935), ('cats', 23993), ('natural', 24105), ('doesn', 24316), ('far', 24346), ('whole', 24364), ('eating', 24417), ('ingredients', 24504), ('using', 24709), ('definitely', 24832), ('k', 24944), ('high', 25169), ('oil', 25213), ('cookies', 25438), ('pack', 25471), ('enjoy', 25558), ('different', 25770), ('old', 25900), ('long', 25930), ('something', 26111), ('green', 26309), ('small', 26371), ('happy', 26470), ('need', 26475), ('ll', 26511), ('salt', 26644), ('say', 26758), ('strong', 26836), ('less', 27296), ('enough', 27372), ('wonderful', 27749), ('fresh', 27805), ('keep', 28015), ('lot', 28484), ('brand', 28817), ('4', 28901), ('got', 29280), ('never', 29520), ('milk', 29725), ('want', 30145), ('right', 30595), ('add', 30657), ('organic', 30828), ('know', 30942), ('treat', 31082), ('years', 31147), ('quality', 31277), ('easy', 31540), ('could', 31981), ('chips', 32063), ('makes', 32109), ('always', 32197), ('without', 32217), ('flavors', 32262), ('give', 32300), ('tasty', 32309), ('every', 33264), ('still', 33268), ('treats', 33727), ('order', 33763), ('5', 33800), ('cat', 33805), ('box', 33928), ('many', 34021), ('excellent', 34433), ('bit', 34600), ('mix', 34911), ('ever', 34912), ('3', 35050), ('hot', 35094), ('bought', 35179), ('think', 35284), ('dogs', 35397), ('re', 36044), ('stuff', 36070), ('recommend', 36217), ('since', 36217), ('two', 36496), ('perfect', 36766), ('snack', 36907), ('healthy', 36914), ('tastes', 37528), ('store', 37656), ('made', 37849), ('1', 38471), ('way', 38476), ('go', 39047), ('nice', 40660), ('loves', 41452), ('day', 41638), ('used', 42040), ('drink', 42060), ('bag', 44237), ('first', 45032), ('found', 45134), ('sweet', 45278), ('favorite', 45280), ('water', 46356), ('sugar', 46419), ('2', 46619), ('free', 48078), ('chocolate', 52378), ('cup', 52451), ('eat', 53117), ('try', 53630), ('even', 54178), ('delicious', 57336), ('better', 57840), ('buy', 58250), ('m', 58614), ('make', 58625), ('tried', 60077), ('well', 61320), ('find', 63153), ('dog', 63341), ('time', 68191), ('little', 69421), ('also', 70045), ('use', 70294), ('price', 70352), ('much', 70683), ('ve', 71991), ('really', 80878), ('would', 82506), ('get', 84809), ('amazon', 85218), ('best', 101359), ('food', 108271), ('flavor', 120831), ('tea', 130919), ('taste', 132704), ('product', 133129), ('one', 138624), ('love', 138818), ('coffee', 147426), ('like', 193545), ('good', 202799), ('great', 219086), ('br', 475248)]
N = [('extremely', 2456), ('expiration', 2459), ('total', 2463), ('line', 2467), ('listed', 2467), ('supposed', 2471), ('wheat', 2476), ('packages', 2477), ('orange', 2477), ('nuts', 2485), ('cocoa', 2497), ('special', 2499), ('close', 2507), ('difference', 2524), ('soda', 2527), ('bite', 2535), ('24', 2536), ('expecting', 2537), ('spicy', 2549), ('plain', 2559), ('20', 2569), ('hours', 2590), ('french', 2595), ('feeding', 2599), ('smaller', 2599), ('name', 2599), ('slightly', 2602), ('later', 2605), ('due', 2606), ('perhaps', 2619), ('gift', 2627), ('items', 2630), ('nasty', 2656), ('soft', 2660), ('ground', 2672), ('canned', 2676), ('family', 2678), ('lemon', 2682), ('brew', 2683), ('absolutely', 2702), ('similar', 2716), ('etc', 2725), ('soy', 2732), ('sodium', 2732), ('single', 2734), ('container', 2736), ('expect', 2738), ('kids', 2738), ('teas', 2741), ('meal', 2761), ('saw', 2764), ('tell', 2767), ('plus', 2772), ('bottom', 2799), ('7', 2811), ('customer', 2819), ('beware', 2819), ('cinnamon', 2822), ('cream', 2833), ('four', 2838), ('picture', 2839), ('overall', 2840), ('completely', 2841), ('change', 2852), ('sent', 2856), ('machine', 2865), ('thinking', 2868), ('rest', 2874), ('especially', 2876), ('feed', 2884), ('help', 2886), ('week', 2894), ('giving', 2898), ('available', 2904), ('noticed', 2912), ('ordering', 2912), ('unless', 2922), ('leaves', 2926), ('called', 2930), ('based', 2933), ('mixed', 2936), ('keurig', 2938), ('non', 2943), ('type', 2944), ('month', 2949), ('longer', 2955), ('past', 2960), ('hoping', 2962), ('pet', 2966), ('experience', 2991), ('delicious', 2997), ('chew', 3008), ('broken', 3009), ('morning', 3023), ('100', 3040), ('brown', 3055), ('home', 3065), ('weeks', 3071), ('batch', 3075), ('ate', 3078), ('serving', 3083), ('red', 3085), ('deal', 3088), ('cannot', 3089), ('part', 3090), ('yet', 3093), ('smells', 3106), ('energy', 3125), ('someone', 3130), ('able', 3141), ('poor', 3143), ('excited', 3148), ('seemed', 3149), ('version', 3151), ('pay', 3152), ('looks', 3156), ('changed', 3163), ('decent', 3178), ('hair', 3185), ('bold', 3203), ('disappointing', 3210), ('dried', 3234), ('inside', 3235), ('ago', 3237), ('pods', 3239), ('fan', 3243), ('believe', 3245), ('cheaper', 3252), ('soup', 3265), ('starbucks', 3270), ('50', 3274), ('ginger', 3286), ('house', 3334), ('loves', 3336), ('reason', 3341), ('href', 3342), ('easy', 3354), ('anyone', 3356), ('looked', 3376), ('gp', 3404), ('started', 3419), ('happy', 3421), ('beef', 3429), ('original', 3431), ('couple', 3438), ('must', 3442), ('honey', 3445), ('extra', 3448), ('ounce', 3459), ('color', 3465), ('cheap', 3466), ('bland', 3477), ('end', 3478), ('http', 3487), ('popcorn', 3494), ('www', 3506), ('please', 3526), ('list', 3557), ('minutes', 3564), ('contains', 3568), ('wish', 3613), ('side', 3634), ('label', 3639), ('loved', 3644), ('cookie', 3666), ('comes', 3673), ('making', 3675), ('return', 3677), ('although', 3696), ('save', 3729), ('care', 3738), ('peanut', 3791), ('grocery', 3794), ('china', 3805), ('salty', 3819), ('prefer', 3821), ('left', 3828), ('variety', 3828), ('idea', 3829), ('description', 3831), ('brands', 3848), ('seem', 3853), ('white', 3856), ('stick', 3892), ('star', 3919), ('light', 3926), ('meat', 3948), ('says', 3978), ('liked', 3993), ('powder', 4036), ('drinking', 4041), ('mouth', 4043), ('let', 4047), ('baby', 4050), ('decided', 4060), ('health', 4061), ('snack', 4063), ('protein', 4075), ('cheese', 4084), ('second', 4113), ('us', 4129), ('top', 4160), ('next', 4171), ('ones', 4171), ('large', 4172), ('juice', 4172), ('beans', 4182), ('worst', 4188), ('cost', 4201), ('others', 4206), ('roast', 4212), ('formula', 4218), ('expected', 4272), ('fact', 4281), ('couldn', 4285), ('months', 4292), ('gluten', 4292), ('year', 4292), ('syrup', 4308), ('open', 4309), ('went', 4344), ('usually', 4362), ('else', 4380), ('ingredient', 4383), ('wrong', 4413), ('blend', 4417), ('cereal', 4425), ('date', 4454), ('okay', 4476), ('jerky', 4479), ('full', 4491), ('aftertaste', 4495), ('artificial', 4498), ('pieces', 4512), ('times', 4532), ('black', 4570), ('calories', 4570), ('come', 4594), ('8', 4602), ('bar', 4630), ('favorite', 4697), ('oz', 4701), ('guess', 4702), ('fat', 4719), ('plastic', 4719), ('several', 4758), ('enjoy', 4775), ('rice', 4780), ('keep', 4791), ('fruit', 4792), ('arrived', 4812), ('rather', 4814), ('dark', 4837), ('tasty', 4848), ('awful', 4855), ('days', 4856), ('butter', 4859), ('added', 4880), ('stale', 4882), ('unfortunately', 4887), ('terrible', 4914), ('com', 4916), ('candy', 4936), ('took', 4941), ('waste', 4957), ('foods', 4962), ('seems', 4974), ('wouldn', 4982), ('definitely', 4997), ('low', 5017), ('local', 5107), ('fresh', 5109), ('came', 5121), ('coconut', 5138), ('horrible', 5159), ('getting', 5207), ('10', 5220), ('sauce', 5272), ('boxes', 5273), ('vanilla', 5275), ('feel', 5325), ('add', 5342), ('things', 5348), ('weak', 5372), ('12', 5388), ('least', 5423), ('gave', 5478), ('amount', 5498), ('opened', 5507), ('case', 5522), ('wanted', 5582), ('far', 5589), ('flavored', 5590), ('always', 5594), ('makes', 5639), ('read', 5661), ('look', 5675), ('corn', 5689), ('treat', 5696), ('need', 5741), ('tasting', 5753), ('bars', 5756), ('per', 5789), ('take', 5795), ('healthy', 5799), ('around', 5863), ('either', 5912), ('cans', 5914), ('wasn', 5915), ('instead', 5945), ('long', 5951), ('without', 5960), ('isn', 5993), ('fine', 6013), ('years', 6099), ('worth', 6191), ('quite', 6197), ('expensive', 6234), ('trying', 6253), ('size', 6259), ('bitter', 6262), ('problem', 6267), ('stars', 6291), ('every', 6292), ('last', 6330), ('shipping', 6369), ('bottle', 6389), ('half', 6405), ('big', 6527), ('kind', 6539), ('regular', 6546), ('review', 6564), ('texture', 6622), ('diet', 6673), ('right', 6701), ('three', 6706), ('milk', 6708), ('purchase', 6708), ('anything', 6717), ('probably', 6750), ('nice', 6885), ('recommend', 6906), ('6', 6913), ('whole', 6923), ('dry', 6932), ('packaging', 6936), ('item', 6948), ('natural', 6981), ('might', 6994), ('using', 7038), ('oil', 7048), ('salt', 7129), ('actually', 7185), ('said', 7230), ('work', 7244), ('cookies', 7317), ('put', 7322), ('company', 7324), ('ever', 7354), ('almost', 7407), ('real', 7422), ('chicken', 7569), ('won', 7574), ('purchased', 7641), ('green', 7651), ('high', 7705), ('treats', 7720), ('looking', 7758), ('cats', 7779), ('mix', 7789), ('cups', 7796), ('pretty', 7842), ('buying', 7862), ('people', 7873), ('new', 7923), ('hot', 8034), ('nothing', 8061), ('reviews', 8064), ('lot', 8090), ('thing', 8110), ('organic', 8162), ('going', 8165), ('smell', 8166), ('enough', 8170), ('another', 8227), ('chips', 8261), ('day', 8317), ('bags', 8357), ('maybe', 8359), ('received', 8411), ('eating', 8426), ('may', 8431), ('ok', 8436), ('away', 8562), ('strong', 8629), ('hard', 8690), ('flavors', 8694), ('k', 8881), ('see', 8884), ('pack', 8919), ('best', 8999), ('though', 9028), ('many', 9044), ('4', 9094), ('small', 9128), ('package', 9154), ('less', 9266), ('store', 9283), ('tasted', 9372), ('stuff', 9477), ('free', 9497), ('d', 9516), ('sure', 9723), ('ll', 9745), ('go', 9750), ('old', 9847), ('quality', 9856), ('bit', 9862), ('dogs', 9898), ('say', 9901), ('products', 9959), ('different', 10002), ('money', 10081), ('re', 10144), ('want', 10399), ('cat', 10508), ('found', 10511), ('since', 10575), ('brand', 10615), ('doesn', 10939), ('never', 11052), ('ordered', 11079), ('back', 11085), ('give', 11268), ('5', 11418), ('disappointed', 11540), ('order', 12012), ('drink', 12033), ('ingredients', 12094), ('however', 12570), ('find', 12570), ('sweet', 13072), ('thought', 13308), ('something', 13383), ('1', 13394), ('know', 13486), ('used', 13505), ('still', 13595), ('two', 13787), ('got', 13947), ('well', 14085), ('could', 14321), ('tastes', 14389), ('way', 14444), ('3', 14579), ('think', 14738), ('sugar', 15016), ('make', 15038), ('chocolate', 15136), ('bag', 15267), ('didn', 15321), ('cup', 15507), ('use', 15762), ('bought', 15866), ('made', 16177), ('love', 16340), ('2', 16348), ('ve', 16454), ('price', 16746), ('try', 17010), ('eat', 17200), ('also', 17232), ('tried', 17610), ('water', 18047), ('box', 18086), ('little', 18467), ('first', 18497), ('bad', 18866), ('time', 18944), ('m', 20195), ('dog', 20209), ('better', 20336), ('great', 21201), ('even', 22504), ('buy', 23674), ('amazon', 24145), ('really', 25864), ('much', 26233), ('get', 26882), ('tea', 29429), ('food', 33558), ('flavor', 40917), ('would', 43334), ('one', 44099), ('coffee', 44551), ('good', 49750), ('product', 54725), ('taste', 58095), ('like', 76097), ('br', 171874)]

def main():
    from config import FINEFOODS
    binary_label = True

    data = scan.scan(FINEFOODS, binary_label=binary_label)
    data = [(tuple(review.split()), score) for review, score in data]
    length = len(data)
    print "data acquired"

    train_data = data[:int(length*.8)]
    test_data = data[int(length*.8):]
 
    PN = P
    PN.extend([elem for elem in N if elem not in P])
    print "len NP: {}".format(len(PN))
    print "making the decision tree"
    decision_tree = dt.train(PN, train_data)
    print "calculating test results"
    test_results = dt.test(decision_tree, test_data)

    print test_results

if __name__ == '__main__':
    main()
