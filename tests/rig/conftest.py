from rig import Rig

import numpy as np
import pytest


@pytest.fixture
def rig_ctc_inputs():
    rod_mount = np.array([23., 28.0, 8.5])
    motor_point = np.array([45.5, -8., 13.])

    motor_angle = 10

    ctc_length = 2.5
    rest_angle = 45
    total_rotation = 45
    motor_torque = 40*12
    motor_rpm = 70

    z_I = 400
    x_I = 300

    return (rod_mount, motor_point,
            motor_angle, motor_torque, motor_rpm,
            ctc_length, rest_angle, total_rotation,
            'ctc', z_I, x_I)


@pytest.fixture
def rig_la_inputs():
    rod_mount = np.array([23., 28.0, 8.5])
    motor_point = np.array([45.5, -8., 13.])

    motor_torque = 40*12
    motor_rpm = 70

    travel = 8
    screw_pitch = 5 / 25.4

    z_I = 400
    x_I = 300

    return (rod_mount, motor_point,
            motor_torque, motor_rpm,
            travel, screw_pitch,
            'linear', z_I, x_I)


@pytest.fixture
def rig_ctc_w_I(rig_ctc_inputs):
    (rod_mount, motor_point,
     motor_angle, motor_torque, motor_rpm,
     ctc_length, ctc_rest_angle, ctc_total_rotation,
     drive, z_I, x_I) = rig_ctc_inputs

    rig = Rig(rod_mount, motor_point,
              motor_angle=motor_angle, motor_torque=motor_torque, motor_rpm=motor_rpm,
              ctc_length=ctc_length, ctc_rest_angle=ctc_rest_angle, ctc_total_rotation=ctc_total_rotation,
              drive=drive, z_I=z_I, x_I=x_I)

    return rig


@pytest.fixture
def rig_la_w_I(rig_la_inputs):
    (rod_mount, motor_point,
     motor_torque, motor_rpm,
     travel, screw_pitch,
     drive, z_I, x_I) = rig_la_inputs

    rig = Rig(rod_mount, motor_point,
              motor_torque=motor_torque, motor_rpm=motor_rpm,
              linear_travel=travel, screw_pitch=screw_pitch,
              drive=drive, z_I=z_I, x_I=x_I)

    return rig


@pytest.fixture
def point_w_length():
    point = np.array([3, 4, 5])
    length = 7.0710678118654755

    return point, length


@pytest.fixture
def points_w_length():
    point1 = np.array([3, 4, 5])
    point2 = np.array([8, 10, 12])
    length = 10.488088481701515

    return point1, point2, length


@pytest.fixture
def ctc_location_info():
    motor_point, motor_angle, ctc_angle = np.array([45.5, -8., 13.]), np.radians(45), np.radians(30)

    ctc_location = np.array([47.03093109, -6.75, 14.53093109])

    return motor_point, motor_angle, ctc_angle, ctc_location


@pytest.fixture
def ctc_angles_w_rod_mount_locations():
    ctc_angle1 = np.radians(25)
    ctc_angle2 = np.radians(35)

    point1 = np.array([23.51940155, 27.37619375, 9.09020167])
    point2 = np.array([23.51940155, 27.74139304, -7.90587521])

    return ctc_angle1, ctc_angle2, point1, point2


@pytest.fixture
def pushrod_lengths_w_mount_locations():
    pushrod1 = 40
    pushrod2 = 45

    rod_mount1 = np.array([25.56061197, 26.14476677, 6.95386843])
    rod_mount2 = np.array([25.56061197, 25.13139163, -10.01590089])

    return pushrod1, pushrod2, rod_mount1, rod_mount2


@pytest.fixture
def rod_mounts_and_pitch_and_roll():
    rod_mount1 = np.array([23.0, 29.0, 8.0])
    rod_mount2 = np.array([23.0, 27.0, -9.0])

    pitch_and_roll = [0.886493844793349, 0.11710874456686428]

    return rod_mount1, rod_mount2, pitch_and_roll


@pytest.fixture
def performance_info():
    d_angle = 1

    pitch = np.array([-1.604185262989378, -1.4987836375112, -1.392116098258006, -1.284461882726448, -1.1761073846530048, -1.0673454032553986, -0.9584743360543039, -0.8497973202014171, -0.7416213255993199, -0.6342562017472609, -0.5280137003173262, -0.4232064400355142, -0.32014686496505523, -0.2191461694485989, -0.1205132060173997, -0.024553378667476217, 0.06843247456212068, -1.4987836375112065, -1.3936352739502258, -1.2872186259931602, -1.1798124002989547, -1.071702482828273, -0.963181188431885, -0.8545464535785815, -0.7461009769235942, -0.6381513117111866, -0.5310069146743484, -0.4249791564448043, -0.32038029842020616, -0.21752243547167166, -0.11671644096406962, -0.018270844770605664, 0.07750925924852499, 0.17032333541557879, -1.3921160982579996, -1.2872186259931602, -1.181050289252671, -1.0738892679239844, -0.9660209456961522, -0.857737160971854, -0.7493353958275127, -0.6411179204189386, -0.5333908820760475, -0.4264633535569164, -0.3206463419724087, -0.21625176390419537, -0.11359139174091183, -0.012975774819373214, 0.08528685526692267, 0.18089169234856958, 0.2735384870593017, -1.2844618827264607, -1.1798124002989483, -1.0738892679239844, -0.9669701446246374, -0.8593399179004014, -0.7512899552736312, -0.6431172960509675, -0.535123792424221, -0.4276151954944811, -0.32090020744941644, -0.2152894857809922, -0.11109461728835608, -0.008627061921566818, 0.09180292673943963, 0.18988740011790667, 0.28532182322752114, 0.3778062161878646, -1.176107384652992, -1.0717024828282793, -0.9660209456961522, -0.8593399179004014, -0.7519437976285385, -0.6441234911596984, -0.5361756036395794, -0.42840157788421557, -0.3211067854384388, -0.2145995687822554, -0.10919025070103618, -0.005190103716508141, 0.09708970731552517, 0.19733920743946573, 0.2952507132676466, 0.3905199440092954, 0.48284716392715576, -1.067345403255405, -0.9631811884318915, -0.857737160971854, -0.7512899552736312, -0.6441234911596856, -0.5365282218264666, -0.4288003285348608, -0.32124085800583635, -0.21415481122500651, -0.10785018799190377, -0.0026369913059737103, 0.10117380601639732, 0.2032713161578046, 0.3033458251865427, 0.4010898955651933, 0.49619948150993287, 0.5883750700946807, -0.9584743360542974, -0.8545464535785752, -0.7493353958275064, -0.6431172960509675, -0.5361756036395794, -0.4288003285348608, -0.32128723930712794, -0.2139369986138643, -0.10705425133193282, -0.0009466675083862911, 0.10407605481455483, 0.20770322407961359, 0.3096242129094044, 0.4095295499131032, 0.5071120241147167, 0.6020678072236584, 0.6940975805488973, -0.8497973202014107, -0.7461009769235878, -0.6411179204189321, -0.5351237924242147, -0.42840157788420924, -0.32124085800583635, -0.21393699861387067, -0.10679029111476177, -0.00010503791876544394, 0.10581140568261901, 0.21064963081567126, 0.31409920965462584, 0.4158497587026346, 0.5155920298811137, 0.6130190192483964, 0.7078270917958165, 0.799717113359207, -0.7416213255993327, -0.6381513117111993, -0.5333908820760411, -0.4276151954944811, -0.3211067854384388, -0.21415481122500651, -0.10705425133193282, -0.00010503791877180505, 0.1063888546552053, 0.2121203709829623, 0.3167803747946321, 0.4200586854973677, 0.5216451450599556, 0.621230709928433, 0.7185085635394157, 0.8131752437391276, 0.9049317808637892, -0.6342562017472609, -0.5310069146743484, -0.4264633535569164, -0.32090020744941644, -0.21459956878224903, -0.10785018799190377, -0.0009466675083862911, 0.10581140568261901, 0.2121203709829623, 0.3176734570773506, 0.42216178405365584, 0.5252754017328454, 0.6267043589493232, 0.7261397976380959, 0.8232750691954523, 0.9178068637326959, 1.0094363518208127, -0.5280137003173325, -0.42497915644479795, -0.3206463419724087, -0.2152894857809922, -0.10919025070103618, -0.002636991305948266, 0.10407605481455483, 0.2106496308156776, 0.3167803747946385, 0.42216178405365584, 0.5264852186276961, 0.6294409413075984, 0.7307191894439878, 0.8300112723844632, 0.9270106887178982, 1.0214142608199042, 1.1129232784154903, -0.4232064400355206, -0.32038029842019344, -0.21625176390419537, -0.11109461728835608, -0.005190103716508141, 0.10117380601640368, 0.20770322407961359, 0.3140992096546322, 0.42005868549736136, 0.5252754017328454, 0.6294409413075984, 0.7322457627932965, 0.8333802737938887, 0.9325359314215368, 1.0294063634496022, 1.1236885029761263, 1.2150837383173085, -0.3201468649650489, -0.21752243547167166, -0.11359139174091183, -0.008627061921566818, 0.09708970731552517, 0.2032713161578046, 0.3096242129094171, 0.4158497587026346, 0.521645145059962, 0.6267043589493232, 0.7307191894439878, 0.8333802737938887, 0.9343781720479277, 1.033404470039799, 1.1301529045091703, 1.224320500367371, 1.3156087234590188, -0.21914616944860527, -0.11671644096406962, -0.012975774819373214, 0.09180292673943963, 0.19733920743945937, 0.3033458251865427, 0.4095295499131032, 0.5155920298811137, 0.621230709928433, 0.7261397976380832, 0.8300112723844632, 0.9325359314215368, 1.033404470039799, 1.132308584752946, 1.22894210090815, 1.3230021160630019, 1.414190153191325, -0.12051320601740607, -0.018270844770612027, 0.08528685526692267, 0.18988740011789396, 0.2952507132676466, 0.4010898955651997, 0.507112024114723, 0.6130190192483964, 0.7185085635394157, 0.8232750691954587, 0.9270106887178982, 1.0294063634496022, 1.1301529045091576, 1.22894210090815, 1.3254678490512244, 1.4194272986721626, 1.510522010074825, -0.024553378667469854, 0.07750925924851226, 0.18089169234856958, 0.28532182322752114, 0.3905199440092954, 0.4961994815099265, 0.6020678072236519, 0.7078270917958228, 0.813175243739134, 0.9178068637326959, 1.021414260819898, 1.1236885029761263, 1.224320500367371, 1.3230021160630019, 1.4194272986721626, 1.5132932312674763, 1.6043014919539544, 0.06843247456216521, 0.17032333541558514, 0.2735384870593017, 0.3778062161878646, 0.48284716392715576, 0.588375070094687, 0.6940975805488973, 0.7997171133592198, 0.9049317808637956, 1.009436351820819, 1.1129232784154968, 1.2150837383173085, 1.3156087234590252, 1.4141901531913315, 1.510522010074825, 1.6043014919539544, 1.6952301757054713])
    roll = np.array([0.0, -0.36389123449825767, -0.731153725638049, -1.1008140657321266, -1.4718852779722682, -1.8433693908577615, -2.214260093624927, -2.583545412368746, -2.950210442947436, -3.3132402311693587, -3.6716221626924264, -4.024349305656875, -4.370422911172707, -4.708855313745716, -5.038672763541007, -5.358918265698529, -5.6686544201971, 0.36389123449825755, 0.0, -0.3672845459124829, -0.7369884395373528, -1.1081239866121846, -1.4796923411607696, -1.8506861606326344, -2.220092305712883, -2.586894580060724, -2.950076511428054, -3.308624157220196, -3.6615289287377153, -4.007790557881489, -4.346419440343789, -4.676440201850231, -4.996894107274446, -5.306842009747547, 0.7311537256380609, 0.3672845459124709, 0.0, -0.36972543292026244, -0.7409034279645437, -1.1125342434300574, -1.483609616238734, -1.8531152793075818, -2.220033800202769, -2.583347358639759, -2.942040566613782, -3.2951033082011136, -3.641533594410694, -3.980340451216796, -4.310546690802836, -4.631191877615486, -4.9413352125870595, 1.1008140657321386, 0.736988439537329, 0.36972543292026244, 0.0, -0.37119889590324995, -0.7428708196089531, -1.11400652933251, -1.4835906427800822, -1.8506046496984796, -2.214029404215511, -2.572848134549604, -2.9260492609522557, -3.272629275296654, -3.6115956104239793, -3.941969521646876, -4.262788796885744, -4.573111246651738, 1.4718852779722809, 1.1081239866121846, 0.7409034279645796, 0.37119889590324995, 0.0, -0.37169211423115445, -0.7428673486888757, -1.1125093930919363, -1.4795984895629077, -1.8431143459582422, -2.202038853844114, -2.5553590373805783, -2.902069922762345, -3.241177430142318, -3.571701286222461, -3.892677766852004, -4.203163111477135, 1.8433693908577244, 1.479692341160781, 1.1125342434300691, 0.7428708196089047, 0.37169211423114246, 0.0, -0.37119462190752833, -0.7408745073218242, -1.1080188646199391, -1.4716061902919528, -1.8306171320637221, -2.184037444152051, -2.530860684484098, -2.870091367210035, -3.20074775531474, -3.5218646879840056, -3.832496892908383, 2.2142600936248056, 1.850686160632706, 1.483609616238734, 1.11400652933251, 0.7428673486888757, 0.37119462190752833, 0.0, -0.36969839567835494, -0.7368787810938582, -1.1005185573011853, -1.4595971906097123, -1.8130991237320533, -2.1600166520501296, -2.4993529064863087, -2.83012476091532, -3.1513657783657187, -3.462128991487481, 2.5835454123686787, 2.220092305712979, 1.8531152793076056, 1.48359064278007, 1.1125093930918657, 0.7408745073218123, 0.369698395678379, 0.0, -0.3671979631180995, -0.7308718627108388, -1.0900000469780393, -1.4435657489629192, -1.7905600388727514, -2.129984750830133, -2.4608554455102065, -2.7822043643866934, -3.093083279392734, 2.9502104429471916, 2.5868945800607546, 2.2200338002027693, 1.85060464969848, 1.4795984895628838, 1.1080188646200462, 0.7368787810938582, 0.3671979631180636, 0.0, -0.3636905085605255, -0.7228508594807239, -1.0764631780423422, -1.4235173214459043, -1.763013950885437, -2.0939673776952232, -2.4154086001108688, -2.726388261383888, 3.313240231169382, 2.9500765114281418, 2.583347358639757, 2.2140294042155104, 1.843114345958242, 1.4716061902918, 1.1005185573011356, 0.7308718627108267, 0.3636905085605256, 0.0, -0.359175975252395, -0.712818492742897, -1.0599163561756881, -1.399468980530799, -1.730489617403232, -2.0520080711633097, -2.3630738303474423, 3.6716221626924144, 3.308624157220282, 2.942040566613782, 2.572848134549605, 2.202038853844114, 1.830617132063484, 1.4595971906097127, 1.0900000469779545, 0.722850859480748, 0.359175975252371, 0.0, -0.35365716212395304, -0.7007832869975912, -1.0403768214127824, -1.371449742312262, -1.693030933019751, -2.004168761162071, 4.024349305656863, 3.6615289287378134, 3.2951033082011016, 2.9260492609522557, 2.5553590373805783, 2.1840374441520387, 1.8130991237320409, 1.4435657489629192, 1.076463178042415, 0.7128184927428848, 0.35365716212395304, 0.0, -0.3471398148315736, -0.686759747115876, -1.0178708456605343, -1.339500897718701, -1.6506973152230071, 4.370422911172696, 4.007790557881501, 3.641533594410694, 3.272629275296654, 2.902069922762346, 2.530860684484096, 2.160016652050129, 1.7905600388727272, 1.4235173214459167, 1.0599163561756026, 0.7007832869975912, 0.3471398148315736, 0.0, -0.3396327105323654, -0.6707685075647197, -0.9924341989787203, -1.303676303655131, 4.708855313745719, 4.346419440343766, 3.980340451216796, 3.6115956104239793, 3.2411774301423057, 2.8700913672100086, 2.499352906486309, 2.1299847508300846, 1.7630139508854492, 1.399468980530763, 1.0403768214127824, 0.686759747115876, 0.3396327105323654, -1.1973852918450886e-14, -0.3311477512822523, -0.6528365272966624, -0.9641120144486047, 5.038672763541055, 4.676440201850255, 4.310546690802883, 3.9419695216468056, 3.5717012862224466, 3.2007477553147456, 2.830124760915386, 2.460855445510225, 2.0939673776953067, 1.7304896174032314, 1.3714497423122622, 1.0178708456605463, 0.6707685075647435, 0.33114775128226426, 0.0, -0.3216999808803258, -0.6329971356628102, 5.358918265698697, 4.996894107274339, 4.6311918776154855, 4.262788796885744, 3.892677766852015, 3.5218646879840048, 3.1513657783657187, 2.7822043643866317, 2.4154086001109416, 2.0520080711632365, 1.693030933019751, 1.339500897718701, 0.9924341989787203, 0.6528365272966624, 0.3216999808803378, 0.0, -0.31130769977983774, 5.668654420197702, 5.306842009747707, 4.941335212587132, 4.573111246651774, 4.203163111477135, 3.832496892908396, 3.462128991487481, 3.0930832793927583, 2.7263882613841717, 2.36307383034751, 2.004168761162226, 1.6506973152230675, 1.3036763036551193, 0.9641120144486166, 0.6329971356627982, 0.3113076997798138, 0.0])
    pitch_torque = np.array([13757.173528732932, 13682.104354695944, 13625.435146756441, 13587.16614641475, 13567.39237955297, 13566.305976107278, 13584.199835861551, 13621.47261822449, 13678.635415229035, 13756.318986686572, 13855.285428768162, 13976.438512933475, 14120.838863417799, 14289.720880926981, 14484.51298189543, 14706.86148474148, 14958.659106105604, 13682.104354695944, 13607.580339259137, 13551.210058293824, 13512.996531129436, 13493.035063160101, 13491.51553888359, 13508.725965532512, 13545.057346184782, 13601.009953179495, 13677.201187360499, 13774.375180474104, 13893.414804549842, 14035.353993878904, 14201.395436761712, 14392.931333555593, 14611.563177167134, 14859.13099751545, 13625.435146755826, 13551.210058295039, 13494.944857542472, 13456.644478133765, 13436.404068924068, 13434.411500250399, 13450.950377651168, 13486.405219854769, 13541.267365634005, 13616.142649266656, 13711.760720857648, 13828.986267543134, 13968.832369250398, 14132.476168128758, 14321.279182067765, 14536.805757217608, 14780.853241685989, 13587.16614641536, 13512.99653113004, 13456.644478133765, 13418.115986455474, 13397.505809640723, 13394.999638007292, 13410.877438238058, 13445.518454368406, 13499.406554575005, 13573.138279877454, 13667.431662621113, 13783.137215108236, 13921.250903502047, 14082.929899050107, 14269.510541738446, 14482.529054796167, 14723.748835591196, 13567.392379553581, 13493.035063160703, 13436.404068924068, 13397.505809640723, 13376.434072757971, 13373.37266328069, 13388.598513425515, 13422.486310654665, 13475.51427894618, 13548.27201838449, 13641.468444173837, 13755.943442124946, 13892.680283468007, 14052.820667786367, 14237.682747047942, 14448.78221251938, 14687.856397819234, 13566.305976107278, 13491.515538884794, 13434.411500249204, 13394.999638006697, 13373.372663281281, 13369.712513283175, 13384.293563545001, 13417.487183558991, 13469.76756493029, 13541.718960050608, 13634.044470384151, 13747.576145119585, 13883.289582273446, 14042.315586665303, 14225.960483158604, 14435.726122774087, 14673.332210338336, 13584.199835861551, 13508.725965532512, 13450.950377651767, 13410.877438238058, 13388.598513425515, 13384.293563544408, 13398.23502715717, 13430.791983820887, 13482.436009964433, 13553.748373479562, 13645.428759353967, 13758.305764277675, 13893.34959883057, 14051.686631031303, 14234.616998803129, 14443.635112446183, 14680.453884566057, 13621.47261822449, 13545.05734618539, 13486.405219856575, 13445.518454369005, 13422.486310654665, 13417.487183558396, 13430.791983821486, 13462.768517346041, 13513.887294306545, 13584.728708409337, 13675.991781805973, 13788.504626716887, 13923.237271701435, 14081.315813319768, 14264.040532128465, 14472.90609355397, 14709.625791538916, 13678.635415229035, 13601.009953179495, 13541.267365634612, 13499.406554575005, 13475.514278945577, 13469.767564929689, 13482.436009964433, 13513.887294304728, 13564.592415457037, 13635.133036480815, 13726.21028349046, 13838.655317883493, 13973.441980516416, 14131.701586292764, 14314.740627805459, 14524.061403533207, 14761.386369080152, 13756.318986686572, 13677.201187360499, 13616.142649267269, 13573.138279878067, 13548.272018383883, 13541.71896005122, 13553.74837348017, 13584.728708408726, 13635.133036480815, 13705.54647137022, 13796.675096113539, 13909.35666386005, 14044.573358428193, 14203.466950578342, 14387.356590788442, 14597.759868231647, 14836.417528723468, 13855.285428769434, 13774.375180472845, 13711.76072085827, 13667.431662621113, 13641.468444176919, 13634.044470385383, 13645.428759354581, 13675.991781805355, 13726.21028349046, 13796.675096113539, 13888.100225032276, 14001.333765641322, 14137.370918131603, 14297.369442208621, 14482.667926955202, 14694.807326306667, 14935.556259009436, 13976.438512933475, 13893.414804548562, 13828.986267545035, 13783.137215106979, 13755.943442123693, 13747.576145115829, 13758.305764277675, 13788.504626716258, 13838.65531788476, 13909.35666386005, 14001.333765641975, 14115.449031079477, 14252.715589996846, 14414.313198698486, 14601.607032358148, 14816.170040184874, 15059.808981181519, 14120.838863416477, 14035.3539938776, 13968.832369247166, 13921.250903501405, 13892.680283465452, 13883.289582274083, 13893.34959883057, 13923.237271701435, 13973.441980516416, 14044.573358428846, 14137.37091813094, 14252.715589996173, 14391.643701392946, 14555.363457334324, 14745.27444325526, 14962.990870787, 15210.36879987058, 14289.720880926305, 14201.39543676238, 14132.476168118832, 14082.929899052735, 14052.820667785056, 14042.315586665303, 14051.68663103065, 14081.315813319768, 14131.701586292764, 14203.466950577675, 14297.369442209298, 14414.313198699865, 14555.363457334324, 14721.763888063875, 14914.957004591108, 15136.60861316064, 15388.636236179655, 14484.51298189543, 14392.931333554221, 14321.279182067086, 14269.51054173912, 14237.682747047942, 14225.96048315793, 14234.616998802458, 14264.040532128465, 14314.740627804098, 14387.356590787756, 14482.667926955202, 14601.607032356735, 14745.274443253818, 14914.957004591848, 15112.14971580618, 15338.581088916722, 15596.24401476674, 14706.861484744346, 14611.563177167842, 14536.80575721691, 14482.529054796167, 14448.782212518689, 14435.726122773394, 14443.635112446183, 14472.90609355397, 14524.061403534604, 14597.759868233059, 14694.807326305952, 14816.170040187055, 14962.990870787742, 15136.608613162161, 15338.581088916722, 15570.71261717073, 15835.086697246186, 14958.659106102641, 14859.130997513259, 14780.853241683093, 14723.748835591196, 14687.856397819234, 14673.332210339762, 14680.453884566057, 14709.625791539633, 14761.38636907943, 14836.417528722739, 14935.556259008697, 15059.80898118077, 15210.368799869813, 15388.63623617887, 15596.244014765933, 15835.086697244526, 16107.35600852867])
    roll_torque = np.array([3979.3712070280835, 3958.3613416792564, 3942.89730915457, 3932.9277385467813, 3928.4322158026976, 3929.420329582798, 3935.9323781655744, 3948.0402949091267, 3965.8479292997545, 3989.495829097943, 4019.1603467717455, 4055.055284338915, 4097.439304105382, 4146.617104461888, 4202.94480163628, 4266.835547634356, 4338.766194310155, 3958.3613416792564, 3937.3327244927814, 3921.7967557137035, 3911.7033099416863, 3907.031272433272, 3907.789658961699, 3914.0174972714753, 3925.784877815489, 3943.194106750537, 3966.3813517918848, 3995.5178304911515, 4030.8158562716785, 4072.5273982156036, 4120.9517006971855, 4176.435500155865, 4239.38383785138, 4310.263180929504, 3942.8973091544735, 3921.796755713704, 3906.1520411960205, 3895.9117286758524, 3891.055443017278, 3891.5912532655097, 3897.5565447228764, 3909.0204593551066, 3926.0831398494774, 3948.878311772212, 3977.5751582583835, 4012.380891081733, 4053.54387016372, 4101.356944240209, 4156.164276429351, 4218.361463869198, 4288.408301531143, 3932.927738546682, 3911.703309941972, 3895.9117286759465, 3885.5024539091532, 3880.453370598849, 3880.7721733440494, 3886.4964227853034, 3897.692376039297, 3914.459466261762, 3936.9294440952417, 3965.26929811958, 3999.6836527746227, 4040.417785727405, 4087.761442205709, 4142.054223052858, 4203.686610957773, 4273.113463834717, 3928.4322158030827, 3907.0312724333694, 3891.055443017849, 3880.4533705986555, 3875.2029526839065, 3875.310596456143, 3880.812580252827, 3891.7755376710297, 3908.296712996451, 3930.5067599419453, 3958.5714289133875, 3992.6935810115388, 4033.116649695367, 4080.128241396414, 4134.065428649682, 4195.315956167407, 4264.331261177794, 3929.4203295822367, 3907.789658961709, 3891.591253264948, 3880.772173343772, 3875.310596456145, 3875.2116946576402, 3880.510959706409, 3891.2740878940576, 3907.5981057762497, 3929.6129396819456, 3957.4834461097917, 3991.4112393892183, 4031.6398025474437, 4078.4556288536023, 4132.193972315389, 4193.245247698647, 4262.054755478319, 3935.93237816577, 3914.0174972715686, 3897.5565447224976, 3886.4964227854975, 3880.812580253377, 3880.510959706317, 3885.62589896197, 3896.222603482985, 3912.397845408336, 3934.2813376475883, 3962.037926227987, 3995.8698109042257, 4036.02035148406, 4082.776740845237, 4136.475014492951, 4197.506181925397, 4266.317816644219, 3948.040294909785, 3925.7848778158655, 3909.0204593552785, 3897.6923760396758, 3891.7755376710297, 3891.2740878931236, 3896.2226034827963, 3906.6859185064804, 3922.7607740121434, 3944.5773693686165, 3972.301263117496, 4006.1360596649197, 4046.326072004357, 4093.160781036405, 4146.978544424735, 4208.172220656159, 4277.19674873197, 3965.847929299761, 3943.1941067503403, 3926.083139849254, 3914.4594662619716, 3908.296712996258, 3907.598105775962, 3912.397845408336, 3922.7607740121434, 3938.78419899004, 3960.5992755955995, 3988.373003995649, 4022.3111627552703, 4062.660900395423, 4109.714286001778, 4163.8145315357815, 4225.359215494299, 4294.808741584782, 3989.4958290979357, 3966.381351791787, 3948.8783117716566, 3936.92944409537, 3930.506759941939, 3929.6129396827, 3934.2813376475883, 3944.5773693685182, 3960.5992755956972, 3982.479712863837, 4010.3880606440225, 4044.5328584988088, 4085.1655892048148, 4132.582985303661, 4187.133918691108, 4249.223172617385, 4319.318700862022, 4019.1603467718455, 3995.5178304914098, 3977.575158257827, 3965.2692981196187, 3958.5714289134526, 3957.483446108814, 3962.03792622749, 3972.3012631181823, 3988.373003995951, 4010.3880606441244, 4038.5188511914002, 4072.9780015316005, 4114.021691043339, 4161.9544270375145, 4217.131201893829, 4279.967005512156, 4350.940747873515, 4055.0552843384994, 4030.815856271571, 4012.3808910812863, 3999.683652773934, 3992.6935810110667, 3991.4112393894425, 3995.8698109039346, 4006.13605966583, 4022.311162755272, 4044.5328584984904, 4072.9780015312913, 4107.8642337544925, 4149.454223349416, 4198.05979395362, 4254.047697123316, 4317.8429254414295, 4389.9389345681075, 4097.439304105257, 4072.5273982156655, 4053.5438701611242, 4040.4177857250625, 4033.1166496935825, 4031.639802547531, 4036.0203514839795, 4046.3260720043686, 4062.66090039407, 4085.165589204188, 4114.021691042794, 4149.454223349098, 4191.733543163331, 4241.181158295999, 4298.1754957668, 4363.156676983036, 4436.635052168228, 4146.617104461574, 4120.951700696961, 4101.356944240355, 4087.761442216567, 4080.128241394887, 4078.4556288536296, 4082.776740845237, 4093.1607810361897, 4109.714286001676, 4132.582985303663, 4161.954427037938, 4198.05979395351, 4241.181158295663, 4291.651416881758, 4349.862430522135, 4416.272830385627, 4491.413210099443, 4202.944801636361, 4176.435500156536, 4156.164276418928, 4142.054223054748, 4134.065428649858, 4132.193972316217, 4136.475014493135, 4146.978544425362, 4163.814531536205, 4187.133918691329, 4217.131201893604, 4254.0476971233165, 4298.17549576703, 4349.862430522016, 4409.518735711897, 4477.621148394337, 4554.727126266459, 4266.835547638797, 4239.3838378546025, 4218.36146387079, 4203.68661095844, 4195.315956167422, 4193.245247698338, 4197.506181926083, 4208.172220658568, 4225.359215495892, 4249.223172619153, 4279.967005512955, 4317.842925441672, 4363.156676983038, 4416.2728303857475, 4477.621148394212, 4547.704828970088, 4627.107982579618, 4338.766194307544, 4310.263180928135, 4288.4083015305105, 4273.1134638345875, 4264.331261177997, 4262.054755478085, 4266.317816644106, 4277.19674873161, 4294.80874158322, 4319.318700860982, 4350.940747871956, 4389.93893456846, 4436.635052168588, 4491.413210099443, 4554.72712626659, 4627.107982579486, 4709.175708555819])
    pitch_omega = np.array([29.308345871910774, 29.469151056548878, 29.591715468696975, 29.67506216197942, 29.718312017543713, 29.72069188990048, 29.681542149841896, 29.600323790288957, 29.47662451410171, 29.310166505314307, 29.100807924376877, 28.848551054468416, 28.55354443881882, 28.216086469412147, 27.83662802497883, 27.41577463133954, 26.954287622974693, 29.469151056548878, 29.630543413859584, 29.753800455128157, 29.837941501069853, 29.882083468444613, 29.885449031870916, 29.847374284500553, 29.767315833001533, 29.64485735897461, 29.47971551172391, 29.271745158470566, 29.020943063469126, 28.727454980889224, 28.39157615147291, 28.013751379469305, 27.59458348919597, 27.134830433046037, 29.59171546869831, 29.753800455125486, 29.8778545786089, 29.962893101261287, 30.008028780001297, 30.012479518919374, 29.97557709155772, 29.896773337820704, 29.77564722067816, 29.61191068468394, 29.405413951446235, 29.156150147196055, 28.864259326897248, 28.530032189920657, 28.15390963852325, 27.73649223453432, 27.278533478897373, 29.675062161978083, 29.83794150106852, 29.962893101261287, 30.04892791260699, 30.095153958422692, 30.10078468803767, 30.065146882214222, 29.98768707717638, 29.867979630804868, 29.70573140021383, 29.50078770854268, 29.25313690979124, 28.962914525056835, 28.630405951761205, 28.256049765732076, 27.840441298232548, 27.384330207084147, 29.718312017542374, 29.88208346844328, 30.008028780001297, 30.095153958422692, 30.142562495123016, 30.149462678705387, 30.115175953307453, 30.03914406527969, 29.92093597718567, 29.760252780049953, 29.556935285233426, 29.310966688426262, 29.022477432220143, 28.691748762173095, 28.31921508319884, 27.90546594651007, 27.45124877853958, 29.72069188990048, 29.885449031868248, 30.012479518922046, 30.100784688039003, 30.14946267870405, 30.157716525273806, 30.12486225632422, 30.050336138502733, 29.933701383961978, 29.774654251020813, 29.57302954936302, 29.32880645604838, 29.042108328188768, 28.713213110156985, 28.342550260653972, 27.930704459951183, 27.478421003507222, 29.681542149841896, 29.847374284500553, 29.975577091556385, 30.065146882214222, 30.115175953307453, 30.124862256325553, 30.09351598794507, 30.0205676988897, 29.905574905158677, 29.748228231013645, 29.54835697072587, 29.305933950594127, 29.02107926758988, 28.69406432033474, 28.32531426970615, 27.915410273176985, 27.465090873238914, 29.600323790288957, 29.767315833000197, 29.8967733378167, 29.987687077175046, 30.03914406527969, 30.050336138504065, 30.020567698888357, 29.949263368860485, 29.83597474354176, 29.680386605763253, 29.482322484019196, 29.241749625173384, 28.958782510981983, 28.633687742349043, 28.26688546571558, 27.858952265266176, 27.41062252120129, 29.47662451410171, 29.64485735897461, 29.775647220676824, 29.867979630804868, 29.92093597718701, 29.933701383963314, 29.905574905158677, 29.835974743545773, 29.724446385911907, 29.570668575160795, 29.37445891273856, 29.135778783286156, 28.85473747715085, 28.53159596796817, 28.16676951986193, 27.76083003215032, 27.31450758883735, 29.310166505314307, 29.47971551172391, 29.61191068468261, 29.705731400212485, 29.760252780051285, 29.774654251019474, 29.748228231012313, 29.680386605764586, 29.570668575160795, 29.41874669807966, 29.224432494868246, 28.987681439474002, 28.708597243221945, 28.387435363700575, 28.02460601123561, 27.62067629824925, 27.176371871403617, 29.10080792437421, 29.27174515847324, 29.405413951444903, 29.50078770854268, 29.556935285226746, 29.57302954936035, 29.548356970724534, 29.482322484020532, 29.37445891273856, 29.224432494868246, 29.032048549970987, 28.79725651490686, 28.52015430131241, 28.200991911818058, 27.840174340361866, 27.438263806167143, 26.99598146917236, 28.848551054468416, 29.0209430634718, 29.15615014719205, 29.25313690979391, 29.31096668842893, 29.328806456056395, 29.305933950594127, 29.24174962517472, 29.135778783283488, 28.987681439474002, 28.79725651490552, 28.564447302542902, 28.289345806000835, 27.972196416295866, 27.613398929753522, 27.213510570304503, 26.773247954461564, 28.553544438821497, 28.727454980891896, 28.86425932690393, 28.96291452505817, 29.022477432225482, 29.04210832818743, 29.02107926758988, 28.958782510981983, 28.85473747715085, 28.70859724322061, 28.520154301313745, 28.28934580600217, 28.0162577927756, 27.701128946857796, 27.344353714923937, 26.94648439485368, 26.50823298929022, 28.21608646941348, 28.391576151471575, 28.530032189940698, 28.63040595175586, 28.691748762175774, 28.713213110156985, 28.694064320336075, 28.633687742349043, 28.53159596796817, 28.38743536370191, 28.200991911816722, 27.97219641629319, 27.701128946857796, 27.388022458837753, 27.033265994389883, 26.637406720646435, 26.201152188655378, 27.83662802497883, 28.013751379471977, 28.153909638524585, 28.25604976573074, 28.31921508319884, 28.34255026065531, 28.325314269707487, 28.26688546571558, 28.166769519864605, 28.024606011236944, 27.840174340361866, 27.613398929756197, 27.344353714926612, 27.033265994388543, 26.68051915726344, 26.286655699290353, 25.85237827891412, 27.415774631334195, 27.594583489194633, 27.736492234535657, 27.840441298232548, 27.905465946511406, 27.930704459952523, 27.915410273176985, 27.858952265266176, 27.76083003214765, 27.620676298246583, 27.43826380616848, 27.2135105703005, 26.946484394852348, 26.63740672064376, 26.286655699290353, 25.894768589805448, 25.462443478135096, 26.954287622980033, 27.13483043305004, 27.278533478902716, 27.384330207084147, 27.45124877853958, 27.47842100350455, 27.465090873238914, 27.410622521199958, 27.314507588838683, 27.17637187140495, 26.995981469173696, 26.7732479544629, 26.508232989291557, 26.20115218865671, 25.852378278915456, 25.462443478137768, 25.03204124789382])
    roll_omega = np.array([101.3225404274667, 101.86033188899081, 102.25982783367328, 102.5190460654084, 102.63636429262253, 102.61055478450415, 102.4407843581703, 102.12661722827744, 101.66804355284309, 101.06540206389106, 100.31946108441699, 99.43144340280743, 98.40292194103239, 97.23588888063583, 95.93273740902501, 94.49625969848884, 92.92964449864924, 101.86033188899081, 102.40435041007143, 102.81001926287334, 103.0753019983028, 103.19855969540008, 103.17853190366709, 103.01435808119847, 102.70557673154049, 102.25213090822571, 101.65437063126748, 100.91307737961874, 100.02937727176197, 99.00485879521986, 97.84147674717622, 96.54165615270547, 95.10816086055358, 93.5441719159827, 102.25982783367579, 102.81001926287333, 103.22178853963518, 103.49310458762375, 103.62227059076363, 103.60800345145886, 103.44942924456488, 103.14604494715748, 102.69777425433185, 102.10494428202534, 101.3682919762966, 100.48896426961544, 99.46851765137428, 98.30892689460714, 97.01252722050671, 95.58213620465179, 94.02089811645048, 102.519046065411, 103.07530199829529, 103.49310458762125, 103.77036297952812, 103.90538462720308, 103.89684887184805, 103.74382377818888, 103.44582411855659, 103.00272706235191, 102.41484022649551, 101.68287944307, 100.80797258060544, 99.7916605120109, 98.63589294546453, 97.34300380617076, 95.91580850698439, 94.35742893617574, 102.63636429261247, 103.19855969539752, 103.62227059074841, 103.90538462720825, 104.04616349725627, 104.0432734265776, 103.89576710085092, 103.60309737731907, 103.16514574218975, 102.58219222753745, 101.85492601068887, 100.984458691631, 99.9723129829272, 98.82042331640189, 97.5311124022771, 96.10718339515475, 94.55175391056218, 102.6105547845188, 103.17853190366684, 103.60800345147379, 103.89684887185548, 104.04327342657754, 104.04592878263935, 103.90384260904271, 103.61644821020826, 103.18358978728796, 102.60552532500418, 101.882927747012, 101.01690249830015, 100.0089342667053, 98.8609504900594, 97.57528390519268, 96.1546430467633, 94.60225715817909, 102.4407843581652, 103.01435808119601, 103.44942924457494, 103.74382377818371, 103.8957671008362, 103.90384260904517, 103.76706622933344, 103.48484700015955, 103.05700389677986, 102.48377413728223, 101.76581029951471, 100.9041883446047, 99.90038822567925, 98.75631845510306, 97.47429842735899, 96.05703542169701, 94.50772711470128, 102.12661722826041, 102.70557673153063, 103.14604494715294, 103.44582411854653, 103.60309737731907, 103.61644821023313, 103.48484700016456, 103.20768252446122, 102.78475370487934, 102.21627369538392, 101.50287535934905, 100.64560813586655, 99.64594865195181, 98.50578112348377, 97.2274140511454, 95.81356913599203, 94.26734931460281, 101.66804355284292, 102.2521309082308, 102.69777425433769, 103.0027270623464, 103.16514574219484, 103.18358978729556, 103.05700389677986, 102.78475370487934, 102.36661356146045, 101.80277577800807, 101.09385446046907, 100.2408773675802, 99.24530003494905, 98.1090100042603, 96.83428427137068, 95.42383959249536, 93.88078125481775, 101.06540206389124, 101.65437063126998, 102.1049442820397, 102.41484022649219, 102.5821922275376, 102.60552532498448, 102.48377413728223, 102.21627369538646, 101.80277577800555, 101.2434535944077, 100.53889895514267, 99.69012840450849, 98.69856954280368, 97.56609883790948, 96.29498550312422, 94.88793212798983, 93.34805508089319, 100.31946108441448, 100.91307737961223, 101.36829197631079, 101.68287944306898, 101.8549260106872, 101.88292774703717, 101.76581029952749, 101.50287535933151, 101.09385446046143, 100.53889895514013, 99.83858311842528, 98.99390565045549, 98.00628929055215, 96.87756246937053, 95.61002034248567, 94.20633371255431, 92.66961408220983, 99.43144340281762, 100.02937727176463, 100.48896426962662, 100.8079725806228, 100.98445869164294, 101.01690249829447, 100.90418834461205, 100.64560813584367, 100.24087736758017, 99.69012840451633, 98.993905650463, 98.15319520223885, 97.16940549220935, 96.04436806277052, 94.78031952313395, 93.37996007781578, 91.84638009997006, 98.4029219410354, 99.00485879521837, 99.46851765143798, 99.79166051206876, 99.97231298297145, 100.00893426670312, 99.90038822568124, 99.64594865195153, 99.24530003498211, 98.69856954281883, 98.0062892905651, 97.16940549221678, 96.18932020562579, 95.067856087995, 93.8072445848488, 92.41015848158773, 90.87968590135718, 97.23588888064317, 97.84147674718156, 98.30892689460363, 98.63589294520253, 98.82042331643888, 98.86095049005873, 98.75631845510306, 98.50578112348894, 98.10901000426277, 97.56609883790944, 96.87756246936065, 96.04436806277302, 95.06785608800253, 93.94984839960705, 92.69258659097454, 91.2987071871628, 89.77129939711622, 95.93273740902316, 96.54165615268995, 97.01252722075, 97.34300380612635, 97.53111240227292, 97.57528390517314, 97.47429842735465, 97.22741405113071, 96.83428427136083, 96.29498550311914, 95.61002034249077, 94.78031952313393, 93.8072445848438, 92.69258659097707, 91.4385501380357, 90.04781481894385, 88.52341508557194, 94.4962596983905, 95.10816086048128, 95.58213620461572, 95.9158085069692, 96.10718339515441, 96.15464304677039, 96.0570354216813, 95.81356913593717, 95.42383959245936, 94.88793212795035, 94.20633371253673, 93.37996007781052, 92.41015848158767, 91.2987071871603, 90.04781481894638, 88.66010771664618, 87.1386623173673, 92.92964449870517, 93.54417191601243, 94.02089811646434, 94.35742893617858, 94.55175391055768, 94.60225715818426, 94.50772711470378, 94.26734931461074, 93.88078125485188, 93.34805508091566, 92.66961408224302, 91.84638009996267, 90.8796859013498, 89.77129939711622, 88.5234150855694, 87.13866231736979, 85.62007980875508])

    return d_angle, pitch, roll, pitch_torque, roll_torque, pitch_omega, roll_omega


@pytest.fixture
def point_to_rotate_and_new_point_quad1():
    angle = np.radians(-30)
    origin_point = np.array([4.0, 5.0, 6.0])
    point = np.array([4.0 + 8.660254037844387, 8.0, 6.0 + 5.0])

    destination = np.array([14, 8.0, 6.0])

    return angle, origin_point, point, destination


@pytest.fixture
def point_to_rotate_and_new_point_quad2():
    angle = np.radians(-30)
    origin_point = np.array([4.0, 5.0, 6.0])
    point = np.array([-4.0 - 8.660254037844387, 8.0, 6.0 + 5.0])

    destination = np.array([-7.92820323, 8.0, 18.66025404])

    return angle, origin_point, point, destination


@pytest.fixture
def point_to_rotate_and_new_point_quad3():
    angle = np.radians(30)
    origin_point = np.array([4.0, 5.0, -6.0])
    point = np.array([-4.0 - 8.660254037844387, 8.0, -6.0 - 5.0])

    destination = np.array([-7.92820323, 8.0, -18.66025404])

    return angle, origin_point, point, destination


@pytest.fixture
def point_to_rotate_and_new_point_quad4():
    angle = np.radians(30)
    origin_point = np.array([4.0, 5.0, -6.0])
    point = np.array([4.0 + 8.660254037844387, 8.0, -6.0 - 5.0])

    destination = np.array([14, 8.0, -6.0])

    return angle, origin_point, point, destination

