import motor.motor_asyncio

''' 
药品说明书基本数据元素:
药品名称 drug_name
    通用名称 drug_name_common
    英文名称 drug_name_eng
    汉语拼音 drug_name_pinyin
成分 compoistion
性状 description
作用类别 action_category
适应症 indication
规格 specification
用法用量dosage_admin
不良反应 adverse_reaction
禁忌 contraindication
警告 warning
注意事项 precaution
孕妇及哺乳期妇女用药 pregnant_care
儿童用药 children_care
老年用药 aged_care
药物相互作用drug_interaction
药物过量 drug_overdose
临床试验 clinical_trial
药理毒理 pharmacological_toxicology
药代动力学 Pharmacokinetic
贮藏 storage
包装 package
有效期 period_validity
执行标准exec_standard
批准文号 license_number
进口药品注册证号imported drug reg
生产企业manufacturing_enterprise
    企业名称 ename 
    生产地址 addr 
    邮编     postcode
    电话号码 tel
    传真号码 fax
    医学咨询电话 consult_tel
    网址 web_site
进口分装企业 sub_packaging_enterprises
    企业名称 ename
    生产地址 addr
    邮编     postcode
    电话号码 tel
OTC等级 otc_level
外用药标记 external_drug

说明书核准日期 chk_date
说明书修订日期 modi_date
录入时间 create_time
更新时间 upd_time
录入人 create_person
更新人 upd_person
'''
db_uri = "mongodb://drug:eastwillpass58@121.36.48.65:27017/drug"
db_conn_args = {
    "zlibCompressionLevel": 7,
    "compressors": "zlib"
}


# 连接数据库
def conn_mongo(db_uri: str, db_conn_args):
    client = motor.motor_asyncio.AsyncIOMotorClient(db_uri, **db_conn_args)
    db = client.get_database("drug")
    return db


# 插入一级分类
async def insert_Qiju_Dihuang_Wan():
    db = conn_mongo(db_uri, db_conn_args)
    await db.drug_insert.drop()
    document = {
        'drug_full_name': '杞菊地黄丸(浓缩丸)-九芝堂股份有限公司',
        'drug_name': '''
            {'common': '杞菊地黄丸',
            'pinyin': 'Qiju Dihuang Wan'}''',
        'compoistion': '枸杞子、菊花、熟地黄、酒萸肉、牡丹皮、山药、茯苓、泽泻。',
        'description': '本品为棕色至棕黑色的浓缩丸;味甜而酸。',
        'indication': '滋肾养肝。用于肝肾阴亏,眩晕耳鸣,羞明畏光,迎风流泪,视物昏花。',
        'specification': '每8丸相当于原药材3克',
        'dosage_admin': '口服。一次8丸,一日3次',
        'adverse_reaction': '尚不明确',
        'contraindication': '尚不明确',
        'precaution': '''
            1、儿童及青年患者应去医院就诊。
            2、脾胃虚寒,大便稀溏者慎用
            3、用药二周后症状未改善,应去医院就诊。
            4、按照用法用量服用
            5、对本品过敏者禁用,过敏体质者慎用。
            6、本品性状发生改变时禁止使用。
            7、儿童必须在成人监护下使用。
            8、请将本品放在儿童不能接触的地方。
            9、如正在使用其他药品,使用本品前请咨询医师或药师''',
        'drug_interaction': '如与其他药物同时使用可能会发生药物相互作用,详情请咨询医师或药师。',
        'storage': '密封。',
        'package': '口服固体药用聚酯瓶包装,每瓶装360丸',
        'period_validity': '36个月',
        'exec_standard': '《中国药典》2015年版第一增补本',
        'license_number': '国药准字Z43020149',
        'modi_date': '2019年01月01日',
        'manufacturing_enterprise': '''
            {'ename': '九芝堂股份有限公司',
             'addr': '湖南省长沙市桐梓坡西路339号',
             'postcode': '410205',
             'tel': '免费咨询电话:8008786588(手机用户请拨打收费电话0731-8449729质量咨询电话:0731-85353895销售电话:0731-84478998传真号码:0731-84478886',
             'web_site': 'www.hnjzt.com',
            }''',
    }

    result = await db.drug_insert.insert_one(document)
    print('inserted %s docs' % result.inserted_id)
    print('insert 杞菊地黄丸(浓缩丸)说明书 success')
