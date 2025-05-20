#################### COLORS CONFIGURATION ###########################

# Primary Colors (Dark to light green shades)
PRIMARY_COLORS = ["#2e7d32", "#43a047", "#66bb6a", "#a5d6a7"]

# Secondary Colors (Alternative green shades)
SECONDARY_COLORS = ["#388e3c", "#4caf50", "#81c784", "#c8e6c9"]

# Neutral Colors (Very light to medium green)
NEUTRAL_COLORS = ["#e8f5e9", "#c8e6c9", "#a5d6a7", "#81c784"]

# Accent Colors (Lime green shades)
ACCENT_COLORS = ["#689f38", "#8bc34a", "#aed581", "#dcedc8"]

# Extended Colors (For charts with many series)
EXTENDED_COLORS = ["#5d4037", "#8d6e63", "#0277bd", "#039be5", "#7b1fa2", "#9c27b0", "#ef6c00", "#f57c00"]

# Text Colors (Very dark to medium green for text)
TEXT_COLORS = ["#1b5e20", "#2e7d32", "#388e3c", "#43a047"]

# Background Colors (Very light green to white)
BACKGROUND_COLORS = ["#e8f5e9", "#f1f8e9", "#f9fbe7", "#ffffff"]

# Chart Colors (Main colors for visualizations with expanded options for multiple series)
CHART_COLORS = [
    PRIMARY_COLORS[0],
    SECONDARY_COLORS[0],
    ACCENT_COLORS[0],
    EXTENDED_COLORS[0],
    EXTENDED_COLORS[2],
    PRIMARY_COLORS[1],
    SECONDARY_COLORS[1],
    ACCENT_COLORS[1],
    EXTENDED_COLORS[1],
    EXTENDED_COLORS[3],
    EXTENDED_COLORS[4],
    EXTENDED_COLORS[6],
]

#################### BPSTAT INDICATORS ###############################
# https://bpstat.bportugal.pt/conteudos/quadros/1895

MAP_INDICATORS_METRICS = {
    "Autonomia Financeira": "%", "Financiamentos obtidos em percentagem do passivo": "%",
    "Custo dos financiamentos obtidos": "%", "VAB em percentagem da produção": "%",
    "Rendibilidade do ativo": "%", "Rendibilidade bruta dos capitais investidos": "%",
    "Cobertura dos gastos de financiamento": "Número", "Financiamentos obtidos em percentagem do ativo": "%",
    "Margem EBITDA em percentagem dos rendimentos": "%", "Rácio dos financiamentos obtidos sobre EBITDA": "Número",
    "Rendibilidade dos capitais próprios": "%", "Margem líquida em percentagem dos rendimentos": "%",
    "Capital próprio em percentagem do ativo": "%", "Liquidez geral": "%",
    "Margem bruta em percentagem dos rendimentos": "%", "Margem EBT em percentagem dos rendimentos": "%",
    "EBIT em percentagem do volume de negócios": "%", "Pressão financeira (Gastos de financiamento/EBITDA)": "%",
                          }

#########################  MEDIUM BPSTAT INDICATORS ##################

MEDIUM_ENTREPRISE_MAP_INDICATORS_KEYS = {
    "Autonomia Financeira": [12606603, 12626412, 12624219, 12615393, 12615893, 12613821,
            12593161, 12594593, 12609645, 12599760, 12594590, 12617758,
            12619173, 12598452, 12603026, 12593876, 12615662, 12605410],

    "Financiamentos obtidos em percentagem do passivo": [12588157, 12592900, 12611362, 12605698, 12616503, 12606153,
            12605683, 12623702, 12604657, 12603331, 12623253, 12630314,
            12612970, 12597354, 12590285, 12628627, 12629789, 12628715],

    "Custo dos financiamentos obtidos": [12612335, 12593500, 12608896, 12610840, 12596431, 12609405,
            12609493, 12590734, 12613387, 12614671, 12625006, 12609796,
            12608103, 12589334, 12587379, 12611131, 12623354, 12621660],

    "VAB em percentagem da produção": [12612589, 12612811, 12628208, 12620257, 12615236, 12612453,
            12628898, 12620057, 12597218, 12608368, 12627614, 12626589,
            12598081, 12626502, 12615835, 12598947, 12618903, 12624877],

    "Rendibilidade do ativo": [12607495, 12611290, 12612702, 12621539, 12593614, 12602954,
            12625639, 12601661, 12616424, 12617481, 12627572, 12613718,
            12597571, 12605675, 12622917, 12596501, 12608016, 12607110],

    "Rendibilidade bruta dos capitais investidos": [12623316, 12626582, 12607534, 12630050, 12594927, 12592064,
            12601321, 12609691, 12622392, 12611607, 12630124, 12610844,
            12614550, 12605483, 12598656, 12610608, 12621468, 12593266],

    "Cobertura dos gastos de financiamento": [12589560, 12590165, 12610993, 12596442, 12613398, 12630460,
            12625687, 12613530, 12597495, 12602769, 12622837, 12626607,
            12600650, 12613727, 12614024, 12599360, 12620024, 12622504],

    "Financiamentos obtidos em percentagem do ativo": [12618225, 12626771, 12594675, 12604367, 12600164, 12604023,
            12621221, 12617466, 12619655, 12604700, 12599784, 12602795,
            12630494, 12593336, 12601120, 12592977, 12629990, 12611805],

    "Margem EBITDA em percentagem dos rendimentos": [12607587, 12591042, 12602639, 12608438, 12626520, 12599617,
            12626541, 12623286, 12620620, 12601451, 12600978, 12615311,
            12593162, 12626480, 12602789, 12629066, 12610509, 12600162],

    "Rácio dos financiamentos obtidos sobre EBITDA": [12614436, 12599137, 12629039, 12609464, 12596422, 12607832,
            12621865, 12598899, 12623280, 12606129, 12603571, 12610001,
            12621742, 12588713, 12590354, 12617296, 12615069, 12607896],

    "Rendibilidade dos capitais próprios": [12595790, 12610787, 12614334, 12614277, 12630825, 12596754,
            12625046, 12594622, 12614836, 12607448, 12618716, 12627986,
            12601550, 12601732, 12627243, 12597557, 12610656, 12591462],

    "Margem líquida em percentagem dos rendimentos": [12594340, 12612743, 12594823, 12587798, 12617832, 12587716,
            12597214, 12624349, 12620651, 12604731, 12615522, 12616930,
            12598506, 12630224, 12612716, 12608678, 12618689, 12601245],

    "Capital próprio em percentagem do ativo": [12632138, 12632446, 12632099, 12632471, 12632410, 12632083,
            12632360, 12632375, 12632348, 12632255, 12632439, 12632168,
            12632502, 12632495, 12632142, 12632340, 12632111, 12632144],


    "Margem bruta em percentagem dos rendimentos": [12589512, 12614265, 12610611, 12628996, 12626627, 12603996,
            12624913, 12630172, 12589979, 12629045, 12589172, 12620524,
            12628135, 12604362, 12611027, 12594812, 12599913, 12630584],

    "Margem EBIT em percentagem dos rendimentos": [12596080, 12615969, 12607929, 12628128, 12607649, 12612604,
            12609360, 12616211, 12611759, 12610271, 12627495, 12604667,
            12621473, 12590914, 12607577, 12600795, 12619274, 12621406],

    "EBITDA em percentagem do volume de negócios": [12598363, 12603493, 12621647, 12613063, 12603800, 12590596,
            12613955, 12614408, 12605133, 12626108, 12590520, 12627374,
            12617045, 12627545, 12601765, 12611341, 12604183, 12609638],

    "Pressão financeira (Gastos de financiamento/EBITDA)": [12617161, 12611543, 12602482, 12622145, 12611802, 12624386,
            12617223, 12630256, 12627205, 12594207, 12619703, 12625363,
            12626687, 12618561, 12620696, 12620907, 12604412, 12600841] ,

    "Liquidez geral": [12623026, 12588216, 12613258, 12611402, 12595465, 12596457,
            12590666, 12624134, 12590811, 12625238, 12628013, 12593728,
            12597459, 12613803, 12608407, 12623434, 12623066, 12605761]
                          }


################# SMALL BPSTAT INDICATORS ############################

SMALL_ENTREPRISE_MAP_INDICATORS_KEYS = {
    "Autonomia Financeira": [12612277,	12600261,	12604116,	12619630,	12594535,	12619871,	12592616,	12605931,	12606434,	12609884,
                             	12611532,	12608550,	12611646,	12592144,	12601411,	12599169,	12594269,	12629865],
    "Financiamentos obtidos em percentagem do passivo": [12602738,	12595080,	12612330,	12600867,	12613416,	12617725,	12589549,	12595206,
                                                         	12590746,	12597722,	12614882,	12598095,	12627017,	12625134,	12604660,	12597037,	12629440,	12592662],

    "Custo dos financiamentos obtidos": [12604315,	12601456,	12615688,	12623183,	12587349,	12604920,	12604924,	12600987,	12604173,	12596555,	12627319,	
                                         12627533,	12601680,	12608719,	12623379,	12588608,	12615446,	12620728],

    "VAB em percentagem da produção": [	12612021,	12615357,	12620147,	12628020,	12594583,	12603702,	12628310,	12588787,	12590314,
                                       	12629616,	12591267,	12596858,	12619824,	12602627,	12590579,	12601804,	12610747,	12621914],

    "Rendibilidade do ativo": [12630036,	12597386,	12613533,	12623889,	12600264,	12601442,	12594491,	12587761,	12598286,	12618001,
                               	12594915,	12624551,	12614699,	12613003,	12610938,	12620731,	12603183,	12621957],

    "Rendibilidade bruta dos capitais investidos": [12595922,	12613834,	12627296,	12625700,	12605660,	12624337,	12624199,	12596775,
                                                    	12619057,	12613630,	12604473,	12613322,	12592014,	12609371,	12597131,	12628052, 12619751,	12620029],

    "Cobertura dos gastos de financiamento": [12594850,	12592877,	12603207,	12588436,	12618618,	12587400,	12623008,	12593733,	12609847,	12628204,	12620790,
                                              	12629206,	12605760,	12592976,	12607666,	12600990,	12592422,	12623136],

    "Financiamentos obtidos em percentagem do ativo": [12605619,	12622439,	12596803,	12588158,	12605951,	12591618,	12609502,	12620406,
                                                       	12618409,	12612520,	12598601,	12628097,	12602328,	12611422,	12619692,	12608656,	12594335,	12598937],

    "Margem EBITDA em percentagem dos rendimentos": [12593537,	12615370,	12619214,	12628524,	12609293,	12589732,	12596987,	12596212,	12620573,	12596744,
                                                     	12611104,	12622624,	12616815,	12597432,	12630235,	12599043,	12627603,	12620255],

    "Rácio dos financiamentos obtidos sobre EBITDA": [12621354,	12610164,	12600423,	12617760,	12596376,	12630569,	12605831,	12601790,	12627403,
                                                      	12603767,	12619765,	12595002,	12620704,	12621341,	12606881,	12607230,	12599703,	12610947],

    "Rendibilidade dos capitais próprios": [12607124,	12589142,	12608034,	12610084,	12622969,	12603369,	12618994,	12629212,	12626403,	12620922,
                                            	12591810,	12589305,	12625317,	12627688,	12602369,	12621511,	12621067,	12608198],

    "Margem líquida em percentagem dos rendimentos": [12609507,	12598902,	12607878,	12606588,	12615908,	12612995,	12597135,	12606837,	12593072,
                                                      	12609164,	12619523,	12592789,	12619769,	12620596,	12609248,	12598976,	12617697,	12619867],

    "Capital próprio em percentagem do ativo": [12632307,	12632480,	12632457,	12632487,	12632356,	12632246,	12632396,	12632402,	12632418,	12632406,
                                                	12632338,	12632320,	12632178,	12632494,	12632372,	12632432,	12632354,	12632091],

    "Margem bruta em percentagem dos rendimentos": [12613905,	12620138,	12607918,	12626779,	12587478,	12602542,	12608297,	12615711,	12612342,	12627871,
                                                    	12630625,	12603969,	12617672,	12621527,	12591105,	12630182,	12597180,	12627632],

    "Margem EBIT em percentagem dos rendimentos": [12591098,	12608715,	12588536,	12609032,	12617568,	12596182,	12614377,	12620608,	12621334,
                                                   	12613882,	12627872,	12617324,	12617397,	12627064,	12599893,	12624335,	12610952,	12600088],

    "EBITDA em percentagem do volume de negócios": [12592617,	12611789,	12600139,	12613033,	12630207,	12610422,	12610856,	12611985,	12589398,
                                                    	12596765,	12593973,	12591710,	12609388,	12608435,	12615461,	12602089,	12604396,	12618714],

    "Pressão financeira (Gastos de financiamento/EBITDA)": [12589197,	12615250,	12606237,	12623496,	12614472,	12599024,	12594699,	12618505,	12616849,
                                                            	12590097,	12611577,	12592913,	12613208,	12624116,	12609037,	12593884,	12621670,	12621158] ,

    "Liquidez geral": [12611121,	12604054,	12588487,	12598196,	12630619,	12608490,	12596945,	12597550,	12594648,	12619314,	12608513,
                       	12606853,	12616856,	12618073,	12596259,	12620725,	12588742,	12606622]
                          }

################# LARGE BPSTAT INDICATORS ############################

LARGE_ENTREPRISE_MAP_INDICATORS_KEYS = {
    "Autonomia Financeira": [12622796,	12601580,	12598415,	12614923,	12630562,	12592744,
                            12616195,	12619905,	12621183,	12624962,	12600103,	12629384,	
                            12630072,	12598282,	12611613,	12594706,	12622249,	12600493],

    "Financiamentos obtidos em percentagem do passivo": [12591387,	12599342,	12602117,	12601218,	12610423,	12590555,
                                                         	12597597,	12587861,	12597966,	12624950,	12602783,	12591675,
                                                                	12614787,	12626757,	12624274,	12602123,	12612975,	12614113],

    "Custo dos financiamentos obtidos": [12592661,	12616155,	12616023,	12593012,	12593068,	12589986,
                                         	12597379,	12588701,	12591697,	12630549,	12619596,	12630768,	
                                            12615957,	12620671,	12602109,	12621561,	12622180,	12616685],

    "VAB em percentagem da produção": [12593468,	12604974,	12599146,	12613274,	12604247,	12629692,	12597683,	12614243,	12600154,
                                       	12616948,	12610694,	12623234,	12625579,	12627341,	12605437,	12623904,	12602174,	12628511],

    "Rendibilidade do ativo": [12629003,	12613559,	12614140,	12610447,	12588459,	12603146,	12617437,	12621303,	12608947,	12628486,
                               	12590471,	12617325,	12600123,	12597300,	12628516,	12601707,	12605617,	12588052],

    "Rendibilidade bruta dos capitais investidos": [12629619,	12629302,	12622093,	12611483,	12594853,	12597399,	12617863,	12613316,	12607696,
                                                    	12624750,	12609788,	12598288,	12594305,	12588781,	12591934,	12617626,	12591555,	12594775],

    "Cobertura dos gastos de financiamento": [12621099,	12607351,	12595381,	12626046,	12610647,	12598671,
    	12627539,	12623772,	12610767,	12623754,	12615001,	12625227,	12620288,	12608691,	12601118,	12595439,	12612096,	12606954],

    "Financiamentos obtidos em percentagem do ativo": [12599231,	12595918,	12598867,	12607099,	12595138,	12599584,	12609408,	12604485,	12612853,
                                                       	12608005,	12605805,	12620883,	12613386,	12619855,	12624716,	12607128,	12619189,	12588884],

    "Margem EBITDA em percentagem dos rendimentos": [12604080,	12622014,	12591370,	12617401,	12629992,	12587741,	12619242,	12593137,	12615660,
                                                     	12593262,	12613783,	12611095,	12615541,	12620847,	12608845,	12615366,	12629473,	12626997],

    "Rácio dos financiamentos obtidos sobre EBITDA": [12610352,	12604450,	12594355,	12602838,	12620403,	12603731,	12589403,	12602553,	12608552,	12599185,
                                                      	12619476,	12628821,	12587823,	12591737,	12612293,	12614179,	12627030,	12592643],

    "Rendibilidade dos capitais próprios": [12600694,	12592698,	12598826,	12593609,	12627957,	12608692,	12619981,	12604062,	12608696,	12601559,	12626104,
                                            	12603659,	12614239,	12629152,	12622750,	12613549,	12587402,	12625056],

    "Margem líquida em percentagem dos rendimentos": [12626014,	12625843,	12590203,	12592975,	12609800,	12599455,	12604058,	12616043,	12613411,
                                                      	12597466,	12590927,	12605608,12626133,	12621211,	12597564, 12598648,	12600706,	12591019],

    "Capital próprio em percentagem do ativo": [12632324,	12632120,	12632454,	12632136,	12632117,	12632248,
                                                        12632149,	12632134,	12632322,	12632332,	12632373,	12632182,
                                                        12632312,	12632412,	12632158,	12632473,	12632508,	12632101],

    "Margem bruta em percentagem dos rendimentos": [12590977,	12624893,	12609477,	12618131,	12625107,	12598333,	12626907,	12622950,	12588962,
                                                    	12607244,	12610019, 12599817,	12624961,	12602643,	12626253,	12622353,	12623793,	12598143],

    "Margem EBIT em percentagem dos rendimentos": [12626939,	12625638,	12589338,	12622373,	12594598,	12628552,	12630209,	12613720,	12620667,	12618046,
                                                   	12618248,	12589306,	12599988,	12591998,	12604295,	12612001,	12589788,	12593158],

    "EBITDA em percentagem do volume de negócios": [12587331,	12611584,	12598461,	12598442,	12593127,	12604533,	12613929,
                                                    	12598235,	12602240,	12627342,	12619828,	12616388,	12598623,	12625504,
                                                            	12626765,	12595071,	12611936,	12624652],

    "Pressão financeira (Gastos de financiamento/EBITDA)": [12604052,	12621073,	12590047,	12625309,	12625673,	12630112,	12602347,	12603714,	12597607,
                                                            	12589683,	12592767,	12608984,	12626905,	12594388,	12602266,	12590131,	12625109,	12600392] ,

    "Liquidez geral": [12621086,	12621470,	12623898,	12598942,	12625689,	12601114,	12603344,	12622307,	12610468,	12614520,
                       	12597668,	12598604,	12620280,	12626112,	12622386,	12630383,	12617088,	12602699]
                          
                          }

################### ALL COMPANIES BPSTAT INDICATORS ##################

ALL_ENTREPRISE_MAP_INDICATORS_KEYS = {
    "Autonomia Financeira": [12613354,	12595543,	12599392,	12589332,	12628684,	12607338,	12622294,	12600040,	12599242,	12603085,
                             	12596281,	12627796,	12612950,	12617892,	12599535,	12622040,	12601084,	12610517],

    "Financiamentos obtidos em percentagem do passivo": [12611012,	12615694,	12612333,	12594312,	12590318,	12608571,	12603749,	12623362,	12618120,
                                                         	12595207,	12630752,	12609760,	12628506,	12630252,	12610381,	12599491,	12596971,	12627452],

    "Custo dos financiamentos obtidos": [12613237,	12628897,	12595413,	12590899,	12601925,	12616701,	12618411,	12595504,	12625145,	12612480,	12624755,
                                         	12610657,	12590180,	12629168,	12619322,	12606730,	12619487,	12610753],

    "VAB em percentagem da produção": [12610227,	12617983,	12624790,	12626019,	12622671,	12600310,	12610102,	12618814,	12591446,	12600957,
                                       	12623470,	12589896,	12590039,	12599351,	12592393,	12596851,	12594289,	12598231],

    "Rendibilidade do ativo": [12587416,	12593009,	12608729,	12600873,	12594987,	12595753,	12590961,	12615868,	12598649,	12611776,
                               	12602724,	12629939,	12588328,	12593279,	12610304,	12620940,	12606596,	12628136],

    "Rendibilidade bruta dos capitais investidos": [12618746,	12614313,	12603289,	12630284,	12621254,	12626560,	12598218,	12620898,	12587440,
                                                    	12595740,	12612643,	12588106,	12596283,	12594209,	12624031,	12610712,	12587809,	12601584],

    "Cobertura dos gastos de financiamento": [12627916,	12624758,	12618879,	12613869,	12618635,	12607564,	12599694,	12596289,	12616500,	12589573,	12613122,
                                              	12627610,	12615667,	12629056,	12604238,	12610594,	12600124,  12597395],
    "Financiamentos obtidos em percentagem do ativo": [12592073,	12604236,	12630595,	12615871,	12610253,	12598075,	12625695,	12612138,	12603776,	12612496,	12618323,
                                                       	12619734,	12619535,	12610439,	12591948,	12588993,	12618042,	12595182],

    "Margem EBITDA em percentagem dos rendimentos": [12601535,	12591161,	12613049,	12591983,	12618427,	12593877,	12591794,	12609944,	12613218,
                                                     	12622594,	12624993,	12596776,	12592653,	12627856,	12593528,	12627284,	12615323,	12597996],

    "Rácio dos financiamentos obtidos sobre EBITDA": [12608106,	12589961,	12588834,	12628753,	12628663,	12609203,	12594493,	12613764,	12594217,	12630347,
                                                      	12596475,	12591893,	12626676,	12627002,	12625012,	12597355,	12593259,	12607269],

    "Rendibilidade dos capitais próprios": [12593458,	12621466,	12598531,	12587522,	12608870,	12621694,	12623091,	12629143,	12620298,	12602212,	12596942,
                                            	12624854,   12620546,	12623670,	12589243,	12615934,	12609418,	12606413],

    "Margem líquida em percentagem dos rendimentos": [12604733,	12619512,	12600866,	12594431,	12596294,	12596841,	12613393,	12600766,	12623143,
                                                      	12594578,	12597003,	12629935,	12622081,	12588208,	12604899,	12625771,	12609173,	12590943],

    "Capital próprio em percentagem do ativo": [12632364,	12632407,	12632106,	12632381,	12632222,	12632108,	12632483,	12632368,
                                                         	12632317,	12632459,	12632306,	12632489,	12632174,	12632162,	12632424,	12632378,	12632344,	12632294],

    "Margem bruta em percentagem dos rendimentos": [12625659,	12620753,   12623294,	12624916,	12598345,	12615278,	12605684,	12611992,	12622978,	12629077,	12607505,
                                                    	12598962,	12625780,	12609673,	12613706,	12616702,	12587557,	12629796],

    "Margem EBIT em percentagem dos rendimentos": [	12623186,	12599479,	12599008,	12599575,	12616666,	12590362,	12613032,	12600355,	12600860,	12630391,
                                                   	12591093,	12613343,	12608357,	12608278,	12605279,	12614137,	12611497,	12602801],

    "EBITDA em percentagem do volume de negócios": [12595707,	12630030,	12607218,	12621570,	12625502,	12589370,	12598383,	12624250,	12593289,	12601285,
                                                    	12590289,	12619480,	12605798,	12627586,	12622853,	12597027,	12604033,	12608736],

    "Pressão financeira (Gastos de financiamento/EBITDA)": [12623864,	12617007,	12596200,	12607274,	12599533,	12606530,	12627526,	12616671,	12609923,	12613355,
                                                            	12627159,	12587463,	12595958,	12627825,	12614342,	12596969,	12599691,	12603330],

    "Liquidez geral": [12616239,	12618620,	12608150,	12607039,	12621163,	12615316,	12599318,	12589008,	12607185,	12590640,	12593894,
                       	12611675,	12630527,	12602839,	12600451,	12607517,	12626322,	12593334]
                          }

####################################################################

indicadores_ecb = {

    "GDP and expenditure components": {
        "Private final consumption": "https://data.ecb.europa.eu/data/datasets/MNA/MNA.A.N.PT.W0.S1M.S1.D.P31._Z._Z._T.XDC.LR.GY",
        "Gross fixed capital formation": "https://data.ecb.europa.eu/data/datasets/MNA/MNA.A.N.PT.W0.S1.S1.D.P51G.N11G._T._Z.XDC.LR.GY",
        "Government final consumption": "https://data.ecb.europa.eu/data/datasets/MNA/MNA.A.N.PT.W0.S13.S1.D.P3._Z._Z._T.XDC.LR.GY",
        "Imports of goods and service": "https://data.ecb.europa.eu/data/datasets/MNA/MNA.A.N.PT.W1.S1.S1.C.P7._Z._Z._Z.XDC.LR.GY",
        "Exports of goods and services": "https://data.ecb.europa.eu/data/datasets/MNA/MNA.A.N.PT.W1.S1.S1.D.P6._Z._Z._Z.XDC.LR.GY",
        "Gross domestic product at market prices": "https://data.ecb.europa.eu/data/datasets/MNA/MNA.A.N.PT.W2.S1.S1.B.B1GQ._Z._Z._Z.XDC_R_B1GQ.Y.GOY",
    },

    "Corporations": {
        "Net value added of Non financial corporations (growth rate)": "https://data.ecb.europa.eu/data/datasets/QSA/QSA.A.N.PT.W0.S11.S1._Z.B.B1N._Z._Z._Z.XDC._T.S.V.GY._T",
        "Gross entrepreneurial income of Non financial corporations": "https://data.ecb.europa.eu/data/datasets/QSA/QSA.A.N.PT.W0.S11.S1._Z.B.B4G._Z._Z._Z.XDC_R_B1G._T.S.V.N._T",
        "Debt securities and loans of Non financial corporations as a ratio of GDP": "https://data.ecb.europa.eu/data/datasets/QSA/QSA.A.N.PT.W0.S11.S1.C.L.LE.F3T4.T._Z.XDC_R_B1GQ_CY._T.S.V.N._T",
        "Debt of Non financial corporations as a ratio of total financial liabilities": "https://data.ecb.europa.eu/data/datasets/QSA/QSA.A.N.PT.W0.S11.S1.N.L.LE.FPT.T._Z.XDC_R_F._T.S.V.N._T",
        "Total financial assets of Non financial corporations as a ratio of total financial assets": "https://data.ecb.europa.eu/data/datasets/QSA/QSA.A.N.PT.W0.S11.S1.N.A.F.F._Z._Z.XDC._T.S.V.FY._T",
        "Total financial liabilities of Non financial corporations as a ratio of total financial assets": "https://data.ecb.europa.eu/data/datasets/QSA/QSA.A.N.PT.W0.S11.S1.N.L.F.F._Z._Z.XDC._T.S.V.FY._T",
        "Gross fixed capital formation of Non financial corporations as a ratio of gross value added": "https://data.ecb.europa.eu/data/datasets/QSA/QSA.A.N.PT.W0.S11.S1.N.D.P51G._Z._Z._Z.XDC_R_B1G_CY._T.S.V.N._T"
    },

    "Households": {
        "Loans granted to households as a ratio of gross disposable income": "https://data.ecb.europa.eu/data/datasets/QSA/QSA.A.N.PT.W0.S1M.S1.N.L.LE.F4.T._Z.XDC_R_B6G_CY._T.S.V.N._T",
        "Gross saving of households as a ratio of adjusted gross disposable income": "https://data.ecb.europa.eu/data/datasets/QSA/QSA.A.N.PT.W0.S1M.S1._Z.B.B8G._Z._Z._Z.XDC_R_B6GA_CY._T.S.V.N._T",
        "Gross disposable income of households (growth rate)": "https://data.ecb.europa.eu/data/datasets/QSA/QSA.A.N.PT.W0.S1M.S1._Z.B.B6G._Z._Z._Z.XDC._T.S.V.GY._T",
        "Total financial assets of households as a ratio of total financial assets": "https://data.ecb.europa.eu/data/datasets/QSA/QSA.A.N.PT.W0.S1M.S1.N.A.F.F._Z._Z.XDC._T.S.V.FY._T",
        "Loans granted to households as a ratio of total financial assets": "https://data.ecb.europa.eu/data/datasets/QSA/QSA.A.N.PT.W0.S1M.S1.N.L.F.F4.T._Z.XDC._T.S.V.FY._T",
        "Gross fixed capital formation of households as a ratio of adjusted gross disposable income": "https://data.ecb.europa.eu/data/datasets/QSA/QSA.A.N.PT.W0.S1M.S1.N.D.P51G._Z._Z._Z.XDC_R_B6GA_CY._T.S.V.N._T",
        "Final consumption expenditure of households (growth rate)": "https://data.ecb.europa.eu/data/datasets/QSA/QSA.A.N.PT.W0.S1M.S1.N.D.P3._Z._Z._Z.XDC._T.S.V.GY._T"
    },

    "Government finance statistics": {
        "Government deficit(-) or surplus(+) (as % of GDP)": "https://data.ecb.europa.eu/data/datasets/GFS/GFS.A.N.PT.W0.S13.S1._Z.B.B9._Z._Z._Z.XDC_R_B1GQ._Z.S.V.N._T",
        "Government primary deficit(-) or surplus(+) (as % of GDP)": "https://data.ecb.europa.eu/data/datasets/GFS/GFS.A.N.PT.W0.S13.S1._Z.B.B9P._Z._Z._Z.XDC_R_B1GQ._Z.S.V.N._T",
        "Government debt (consolidated) (as % of GDP)": "https://data.ecb.europa.eu/data/datasets/GFS/GFS.A.N.PT.W0.S13.S1.C.L.LE.GD.T._Z.XDC_R_B1GQ._T.F.V.N._T"
    },

    "Labour market indicators": {
        "Gross fixed capital formation": "https://data.ecb.europa.eu/data/datasets/MNA/MNA.A.N.PT.W0.S1.S1.D.P51G.N11G._T._Z.XDC.LR.GY",
    }
}

# 
MAP_CATEGORIES_ECB_INDICADORS_URLS = {

    "GDP and expenditure components": {
        "Private final consumption": "https://data.ecb.europa.eu/data/datasets/MNA/MNA.A.N.PT.W0.S1M.S1.D.P31._Z._Z._T.XDC.LR.GY",
        "Gross fixed capital formation": "https://data.ecb.europa.eu/data/datasets/MNA/MNA.A.N.PT.W0.S1.S1.D.P51G.N11G._T._Z.XDC.LR.GY",
        "Government final consumption": "https://data.ecb.europa.eu/data/datasets/MNA/MNA.A.N.PT.W0.S13.S1.D.P3._Z._Z._T.XDC.LR.GY",
        "Imports of goods and service": "https://data.ecb.europa.eu/data/datasets/MNA/MNA.A.N.PT.W1.S1.S1.C.P7._Z._Z._Z.XDC.LR.GY",
        "Exports of goods and services": "https://data.ecb.europa.eu/data/datasets/MNA/MNA.A.N.PT.W1.S1.S1.D.P6._Z._Z._Z.XDC.LR.GY",
        "Gross domestic product at market prices": "https://data.ecb.europa.eu/data/datasets/MNA/MNA.A.N.PT.W2.S1.S1.B.B1GQ._Z._Z._Z.XDC_R_B1GQ.Y.GOY",
    },

    "Corporations": {
        "Net value added of Non financial corporations (growth rate)": "https://data.ecb.europa.eu/data/datasets/QSA/QSA.A.N.PT.W0.S11.S1._Z.B.B1N._Z._Z._Z.XDC._T.S.V.GY._T",
        "Gross entrepreneurial income of Non financial corporations": "https://data.ecb.europa.eu/data/datasets/QSA/QSA.A.N.PT.W0.S11.S1._Z.B.B4G._Z._Z._Z.XDC_R_B1G._T.S.V.N._T",
        "Debt securities and loans of Non financial corporations as a ratio of GDP": "https://data.ecb.europa.eu/data/datasets/QSA/QSA.A.N.PT.W0.S11.S1.C.L.LE.F3T4.T._Z.XDC_R_B1GQ_CY._T.S.V.N._T",
        "Debt of Non financial corporations as a ratio of total financial liabilities": "https://data.ecb.europa.eu/data/datasets/QSA/QSA.A.N.PT.W0.S11.S1.N.L.LE.FPT.T._Z.XDC_R_F._T.S.V.N._T",
        "Total financial assets of Non financial corporations as a ratio of total financial assets": "https://data.ecb.europa.eu/data/datasets/QSA/QSA.A.N.PT.W0.S11.S1.N.A.F.F._Z._Z.XDC._T.S.V.FY._T",
        "Total financial liabilities of Non financial corporations as a ratio of total financial assets": "https://data.ecb.europa.eu/data/datasets/QSA/QSA.A.N.PT.W0.S11.S1.N.L.F.F._Z._Z.XDC._T.S.V.FY._T",
        "Gross fixed capital formation of Non financial corporations as a ratio of gross value added": "https://data.ecb.europa.eu/data/datasets/QSA/QSA.A.N.PT.W0.S11.S1.N.D.P51G._Z._Z._Z.XDC_R_B1G_CY._T.S.V.N._T"
    },

    "Households": {
        "Loans granted to households as a ratio of gross disposable income": "https://data.ecb.europa.eu/data/datasets/QSA/QSA.A.N.PT.W0.S1M.S1.N.L.LE.F4.T._Z.XDC_R_B6G_CY._T.S.V.N._T",
        "Gross saving of households as a ratio of adjusted gross disposable income": "https://data.ecb.europa.eu/data/datasets/QSA/QSA.A.N.PT.W0.S1M.S1._Z.B.B8G._Z._Z._Z.XDC_R_B6GA_CY._T.S.V.N._T",
        "Gross disposable income of households (growth rate)": "https://data.ecb.europa.eu/data/datasets/QSA/QSA.A.N.PT.W0.S1M.S1._Z.B.B6G._Z._Z._Z.XDC._T.S.V.GY._T",
        "Total financial assets of households as a ratio of total financial assets": "https://data.ecb.europa.eu/data/datasets/QSA/QSA.A.N.PT.W0.S1M.S1.N.A.F.F._Z._Z.XDC._T.S.V.FY._T",
        "Loans granted to households as a ratio of total financial assets": "https://data.ecb.europa.eu/data/datasets/QSA/QSA.A.N.PT.W0.S1M.S1.N.L.F.F4.T._Z.XDC._T.S.V.FY._T",
        "Gross fixed capital formation of households as a ratio of adjusted gross disposable income": "https://data.ecb.europa.eu/data/datasets/QSA/QSA.A.N.PT.W0.S1M.S1.N.D.P51G._Z._Z._Z.XDC_R_B6GA_CY._T.S.V.N._T",
        "Final consumption expenditure of households (growth rate)": "https://data.ecb.europa.eu/data/datasets/QSA/QSA.A.N.PT.W0.S1M.S1.N.D.P3._Z._Z._Z.XDC._T.S.V.GY._T"
    },

    "Government finance statistics": {
        "Government deficit(-) or surplus(+) (as % of GDP)": "https://data.ecb.europa.eu/data/datasets/GFS/GFS.A.N.PT.W0.S13.S1._Z.B.B9._Z._Z._Z.XDC_R_B1GQ._Z.S.V.N._T",
        "Government primary deficit(-) or surplus(+) (as % of GDP)": "https://data.ecb.europa.eu/data/datasets/GFS/GFS.A.N.PT.W0.S13.S1._Z.B.B9P._Z._Z._Z.XDC_R_B1GQ._Z.S.V.N._T",
        "Government debt (consolidated) (as % of GDP)": "https://data.ecb.europa.eu/data/datasets/GFS/GFS.A.N.PT.W0.S13.S1.C.L.LE.GD.T._Z.XDC_R_B1GQ._T.F.V.N._T"
    },

    "Labour market indicators": {
        "Gross fixed capital formation": "https://data.ecb.europa.eu/data/datasets/MNA/MNA.A.N.PT.W0.S1.S1.D.P51G.N11G._T._Z.XDC.LR.GY",
    }
}


MAP_CATEGORIES_ECB_INDICADORS = {

    "GDP and expenditure components": [
        "Private final consumption", "Government final consumption",
        "Imports of goods and service", "Exports of goods and services", "Gross domestic product at market prices"
    ],

    "Corporations": [
        "Net value added of Non financial corporations (growth rate)",
        "Gross entrepreneurial income of Non financial corporations",
        "Debt securities and loans of Non financial corporations as a ratio of GDP",
        "Debt of Non financial corporations as a ratio of total financial liabilities",
        "Total financial assets of Non financial corporations as a ratio of total financial assets",
        "Total financial liabilities of Non financial corporations as a ratio of total financial assets",
        "Gross fixed capital formation of Non financial corporations as a ratio of gross value added"
    ],

    "Households": [
        "Loans granted to households as a ratio of gross disposable income",
        "Gross saving of households as a ratio of adjusted gross disposable income",
        "Gross disposable income of households (growth rate)",
        "Total financial assets of households as a ratio of total financial assets",
        "Loans granted to households as a ratio of total financial assets",
        "Gross fixed capital formation of households as a ratio of adjusted gross disposable income",
        "Final consumption expenditure of households (growth rate)"
        ],

    "Government finance statistics": [
        "Government deficit(-) or surplus(+) (as % of GDP)",
        "Government primary deficit(-) or surplus(+) (as % of GDP)",
        "Government debt (consolidated) (as % of GDP)"],

}

MAP_OTHER_BPSTAT_INDICATORS = {
    "CPI (Consumer Price Index) MA12": {
        'url': 5721550
        }
    }

MAP_OTHER_ECB_INDICATORS = {
        "Unemployment rate":{
            'periodicity': "Monthly",
            'url': "https://data.ecb.europa.eu/data/datasets/LFSI/LFSI.M.PT.S.UNEHRT.TOTAL0.15_74.T"
            },
        "Labour Productivity (per persons)": {
            'url': "https://data.ecb.europa.eu/data/datasets/MNA/MNA.Q.S.PT.W0.S1.S1._Z.LPR_PS._Z._T._Z.XDC.LR.GY",
            'periodicity': "Quarterly"
            }
    }


################################################################################################################3


ldp_sectors = ['All', 'Agricult & fishing', 'Mining and quarrying', 'Manufacturing', 'Electricity and gas', 'Water and waste',
               'Construction', 'Trade', 'Transport and storage', 'Hotels and similar', 'Information and communication', 'Real estate', 
               'Administrative activities', 'Education', 'Health and social', 'Shows and sports', 'Professional and scientific']

medium_all_columns = ['Date', 
       'Capital ratio-Medium-%',
       'Financial debt (% liabilities)-Medium',
       'Cost of financial debt-Medium-%',
       'GVA (% output)-Medium',
       'Return on assets-Medium-%',
       'EBITDA / invested capital-Medium-%',
       'Financing expenses coverage ratio-Medium',
       'Financial debt (% assets)-Medium',
       'EBITDA margin (% income)-Medium',
       'Financial debt over EBITDA-Medium',
       'Return on equity-Medium-%',
       'Net income (% income)-Medium',
       'Equity (% assets)-Medium',
       'Gross profit (% income)-Medium',
       'EBIT margin (% income)-Medium',
       'EBITDA (% turnover )-Medium',
       'Financial pressure-Medium-%',
       'Current ratio-Medium-%']

small_all_columns = ['Date', 
       'Capital ratio-Small-%',
       'Financial debt (% liabilities)-Small',
       'Cost of financial debt-Small-%',
       'GVA (% output)-Small',
       'Return on assets-Small-%',
       'EBITDA / invested capital-Small-%',
       'Financing expenses coverage ratio-Small',
       'Financial debt (% assets)-Small',
       'EBITDA margin (% income)-Small',
       'Financial debt over EBITDA-Small',
       'Return on equity-Small-%',
       'Net income (% income)-Small',
       'Equity (% assets)-Small',
       'Gross profit (% income)-Small',
       'EBIT margin (% income)-Small',
       'EBITDA (% turnover )-Small',
       'Financial pressure-Small-%',
       'Current ratio-Small-%']

large_all_columns = ['Date', 
       'Capital ratio-Large-%',
       'Financial debt (% liabilities)-Large',
       'Cost of financial debt-Large-%',
       'GVA (% output)-Large',
       'Return on assets-Large-%',
       'EBITDA / invested capital-Large-%',
       'Financing expenses coverage ratio-Large',
       'Financial debt (% assets)-Large',
       'EBITDA margin (% income)-Large',
       'Financial debt over EBITDA-Large',
       'Return on equity-Large-%',
       'Net income (% income)-Large',
       'Equity (% assets)-Large',
       'Gross profit (% income)-Large',
       'EBIT margin (% income)-Large',
       'EBITDA (% turnover )-Large',
       'Financial pressure-Large-%',
       'Current ratio-Large-%']

all_companies_all_columns = ['Date', 
       'Capital ratio-Corporations-%',
       'Financial debt (% liabilities)-Corporations',
       'Cost of financial debt-Corporations-%',
       'GVA (% output)-Corporations',
       'Return on assets-Corporations-%',
       'EBITDA / invested capital-Corporations-%',
       'Financing expenses coverage ratio-Corporations',
       'Financial debt (% assets)-Corporations',
       'EBITDA margin (% income)-Corporations',
       'Financial debt over EBITDA-Corporations',
       'Return on equity-Corporations-%',
       'Net income (% income)-Corporations',
       'Equity (% assets)-Corporations',
       'Gross profit (% income)-Corporations',
       'EBIT margin (% income)-Corporations',
       'EBITDA (% turnover )-Corporations',
       'Financial pressure-Corporations-%',
       'Current ratio-Corporations-%']



############ CSS STYLES FOR THE CONTAINER AND BUTTONS ############

container_style_html = """
    <style>
        .gpt-container {
            background-color: #ffffff;
            border-radius: 10px;
            padding: 25px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            margin-bottom: 30px;
        }
        .gpt-button {
            background: linear-gradient(135deg, #6e8efb, #a777e3);
            color: white;
            border: none;
            padding: 12px 24px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 10px 0;
            cursor: pointer;
            border-radius: 25px;
            transition: all 0.3s ease;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        .gpt-button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 8px rgba(0,0,0,0.15);
            background: linear-gradient(135deg, #5e7cea, #9d68e1);
        }
        .gpt-textarea {
            border-radius: 10px;
            border: 2px solid #e0e0e0;
            padding: 15px;
            font-size: 16px;
        }
        .gpt-toggle {
            margin: 15px 0;
        }
        .gpt-response {
            background-color: #f8f9fa;
            border-radius: 10px;
            padding: 20px;
            margin-top: 20px;
            border-left: 5px solid #6e8efb;
        }
    </style>"""
