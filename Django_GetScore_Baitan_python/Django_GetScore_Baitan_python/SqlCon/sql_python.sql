
set names utf8;
set names utf8;
SET FOREIGN_KEY_CHECKS = 0;

drop table IF exists bt_problems_sy;
create table bt_problems_sy (
  id int AUTO_INCREMENT,
  title varchar(100),
  options varchar(200),
  flag varchar(10),
  primary key (id)
);

drop table IF exists bt_record;
create table bt_record (
  id int AUTO_INCREMENT,
  award int not null,
  win_date datetime default '2018-09-28 00:00:00',
  primary key (id)
);
insert into bt_problems_sy(title, options, flag)
select '入户拜访的6步骤中属于第4步的是？','A.预约沟通B.持续关怀C.适时销售D.提高粘度','B'
union all select '明明妈妈是店里顾客，但是宝宝一直吃母乳，你对母乳顾客的服务是：每月至少一条育儿短信，3个月电话跟进一次，至少到宝宝几岁？','A.3岁<br>B.1岁<br>C.2岁<br>D.半岁','C'
union all select '为便于营养顾问管理会员和分类服务，根据会员活跃的月数（会员购买月数），把会员分为A、B、C、D四类会员，A类会员（价值会员）是指购买大于10个月次（不要求连续月）的会员，B类会员（忠诚会员）是指购买6-9个月次的会员，C类会员（游离会员）是指购买2-5个月次的会员，D类会员（潜力会员）是指购买1个月次的会员。B类会员（忠诚会员）是指？','A.购买大于10个月次（不要求连续月）的会员<br>B.购买6-9个月次的会员<br>C.购买2-5个月次的会员<br>D.购买1个月次的会员','B'
union all select '顾客来买奶粉，了解到她宝宝有点便秘，为了让顾客体会到宝宝能够受益，你使用FABE法介绍膳食纤维：“这款奶粉含有膳食纤维，它可以促进宝宝肠道健康，避免宝宝上火，减轻便秘，让您的宝宝更健康，您看我们这里很多宝宝都在用——”。FABE法是通过(______)的销售方法。','A.介绍产品特征转化为顾客利益<br>B.客户资料本、掌中宝资料<br>C.顾客利益<br>D.流利的口才','A'
union all select '入户拜访的6步骤中属于第6步的是？','A.持续关怀<br>B.预约沟通<br>C.适时销售<br>D.提高粘度','D'
union all select '哪个肢体信号说明消费者可能想要购买了？','A.看头顶<br>B.摸下巴<br>C.环顾四周<br>D.微笑','B'
union all select '下列属于客户沟通时灵活运用语言技巧的是？','A.用命令的口气<br>B.对话中疑问的语气较多<br>C.说话生硬<br>D.表达不同的观点时先对顾客的观点表示理解','D'
union all select '介绍产品的FABE法中F代表(______)','A.优点<br>B.利益<br>C.
特点<br>D.证据','C'
union all select '客户说朋友家宝宝都是喝的**牌子的奶粉，我也想要**品牌，面对这种从众型客户，应借助(______)打动客户？','A.原装进口；专属性<br>B.客户资料本、掌中宝资料<br>C.顾客利益<br>D.流利的口才','B'
union all select '“这款奶粉含有膳食纤维，它可以促进宝宝肠道健康，避免宝宝上火，减轻便秘，让您的宝宝更健康，您看我们这里很多宝宝都在用——”。这是使用FABE法介绍产品，介绍产品的FABE法中B代表(______)。','A.利益<br>B.优点<br>C.
特点<br>D.证据','A'
union all select '掌中宝“会员管理”中“我的会员”可以通过哪些内容进行筛选？','A.全部会员（显示全部会员）、月龄分类、喂养类型、自定义分类<br>B.产品分类、段位分类、<br>C.注册时间、积分分类<br>D.会员类型、会员级别、','ABCD'
union all select '“我是华西分公司营养顾问杨晓红，我的第销售秘诀之一是“持续关怀和服务。每逢过节过生日，都送上祝福短信，情况允许的话，可以买一份小礼品送到家里，顾客会感到欣喜，觉得我们是真正的专业、关爱、可信赖！”你觉得这位营养顾问哪里值得我们学习？','A.关怀<br>B.关爱<br>C.服务<br>D.付出','ABCD'
union all select '销售的第一步是接近顾客，接近顾客时，自然，让消费者舒适，感觉被帮助，例如当消费者：①在相关产品附近突然停下脚步时；②看相关产品或若有所思时；③眼光与我们眼光相碰时；④伸手触摸相关产品时；⑤眼睛在搜寻相关产品时。我们在这些时候可以插入问话，不管她买不买产品，都要提供帮助。有位顾客走到奶粉区打量某产品，你上去接近顾客。请问接近顾客的最佳时机有哪些？','A.在相关产品附近突然停下脚步时<br>B.眼光与我们眼光相碰时<br>C.伸手触摸相关产品时<br>D.眼睛在搜寻相关产品时','ABCD'
union all select '顾客带着奶粉到超市找你说：“我说要新日期的，你说新老都一样，让我帮你处理老货，结果喝了这奶粉后，宝宝大便发灰。”这时，你该如何处理？','A.安抚、关心宝宝<br>B.分析原因；（辅食、消化不良也会引起大便发灰）<br>C.给出解释<br>D.强调奶粉品质','ABCD'
union all select '“我是营养顾问袁明芬，现在很多人思想超前行动滞后，以至于最终的结果是失败的。凡事想到了，就去行动，结果没准会超出自己想象呢！销售就是这样，需要我们踏踏实实认认真真走好每一步，不吝惜力气、不吝惜汗水、不吝惜勇气、不吝惜跌倒，只有经过风雨的洗礼，梦想的种子才会顽强的成长起来。让我们不断地努力奋斗，坚持不懈，勇往直前，携手共创新的华丽篇章。”你觉得这位营养顾问或她的说法哪里值得我们学习？','A.执行力强<br>B.不吝惜力气、不吝惜汗水<br>C.不吝惜勇气、不吝惜跌倒<br>D.坚持不懈，勇往直前','ABCD'
union all select '顾客打电话说：“我今天中午给宝宝冲调奶粉的时候，发现奶粉里有结块，有质量问题吧？”您该如何处理？','A.安抚<br>B.解释结块原因<br>C.奶粉保存注意事项<br>D.其他表现（自然、大方、自信、亲和、微笑等）','ABCD'
union all select '小高是我们忠实的消费者，有一次他问营养顾问:“你们圣元怎么也不做个广告呢？”请问您该怎样回答？','A.圣元注重品质，注重口碑营销<br>B.圣元更注重奶粉的研究和配方的提升，我们把资源主要投在了提升奶粉品质上，奶粉好才最重要。<br>C.在电视上也有做广告；(只是各个频道播放时间有差异)<br>D.传播官网、官微；让消费者随时了解圣元最新动态，更专业帮消费者解决育儿难题','ABCD'
union all select '一位消费者来到超市找您，说：“奶粉冲好了总有泡沫”，请问您该如何解答？','A.安抚<br>B.分析起泡原因；（①奶粉中含有磷脂容易产生气泡，是正常的物理反应；②婴幼儿奶粉不允许添加化学消泡剂；③奶粉冲调时要横向搓动，不要上下晃动）<br>C.正确冲调方法；（开水冷却到40-60度,先放水，再放奶粉，一平勺奶粉（4.3g)放30毫升水）<br>D.其他表现（自然、大方、自信、亲和、微笑等）','ABCD'
union all select '营养顾问在和顾客聊天时说到“圣元国际”，客户说：“圣元不是国产品牌吗？你怎么说是“圣元国际”呢？”请你给顾客介绍下圣元主要机构分布情况：','A.生产基地：在北京<br>B.总部：在美国<br>C.原料基地：在法国<br>D.研发中心：在北京','BCD'
union all select '有一个妈妈怒气冲冲的过来，说她买的奶粉吃了一半发现有个虫子在里面，你处理客诉需要注意以下哪几点？','A.跟客户在卖场内认真解释<br>B.聆听顾客的讲话，对顾客的反对意见表示理解，但非认同<br>C.尽量带顾客远离奶粉区<br>D.不与顾客发生争执','BCD'
union all select '圣元实验室的标准是CNAS国家级实验室','A.正确<br>B.错误','A'
union all select '圣元在海关享有最高信用等级是海关总署授予的双B企业称号。','A.正确<br>B.错误','B'
union all select '圣元的生产车间是按照什么GMP20万级的生成标准建立的，圣元采用的是中国食品安全管理体系。','A.正确<br>B.错误','B'
union all select '圣元的免费服务电话是8009902829；圣元服务电话4008182828可用手机拨打，收取市话费。','A.正确<br>B.错误','B'
union all select '客户购买产品3天之后打第一次回访电话。','A.正确<br>B.错误','B'
union all select '情感沟通，事例说明，肯定陈词，可以在最短的时间内打动消费者。','A.正确<br>B.错误','A'
union all select '处理客户异议的六字原则是：认同、赞美、鼓励','A.正确<br>B.错误','B'
union all select '对质量满意是一件事情，没有下单又是一件事情。客户是要喜欢比较价格、还是预算有限、还是客户对产品不太了解呢？您要了解客户的需求，或许您会发现客户想的可能跟您想的不一样','A.正确<br>B.错误','A'
union all select '利用掌中宝查询会员归属：点击主界面“+”-会员积分-输入手机号-信息确认界面的“关联对象”就是目前归属顾问','A.正确<br>B.错误','A'
union all select '“我是云南营养顾问夏石莲，我认为作为一个营养顾问，应该把“以人为本，顾客第一，服务至上”作为自己的服务宗旨，把“发展新顾客，留住新老客户”作为做好工作的主要思路。踏踏实实，一步一个脚印，认真做好每个客户的基本资料，完成公司交给我们的每一项促销任务，使自己所在卖场的销量逐步上升。在日常工作中，我们要坚持服务，坚持回访，坚持维护，坚持开发。同时我们一定要熟悉奶粉的营养知识、育儿常识，以专业要求才能打动一个又一个顾客，我们的销量份额才会不断增长！”你觉得这位营养顾问说得对吗？','A.正确<br>B.错误','A'
union all select '入户拜访的6步骤中属于第2步的是？','A.预约沟通<br>B.持续关怀<br>C.适时销售<br>D.提高粘度','A'
union all select '（会员数量与销量的计算）您的顾客平均每人每月消费500元，您目前有160位顾客，月销量是8万元。如果您希望月销量达到9万元的话，您的顾客数量应该有多少？','A.200位<br>B.160位<br>C.180位<br>D.220位','C'
union all select '聪聪妈妈是店里顾客，但是宝宝一直吃母乳，对于有母乳未购买产品的客户应当每月(______)条育儿短信、(______)个月电话跟进一次。','A.3;3<br>B.3;6<br>C.1;3<br>D.1;6','C'
union all select '每当新客户来购买奶粉，都做好充分准备对新顾客进行服务，这样才能变成我们的老客户，带来连续销售。下列哪种做法是不正确的？','A.留取客户资料<br>B.催促购买<br>C.发送服务短信<br>D.邀约下次购买时间','B'
union all select '顾客说我就和**品牌的奶粉，面对这种客户，应对方法是借助(______)、差异性、(______)等。','A.讲究原装进口；专属性<br>B.客户资料本、掌中宝资料<br>C.顾客利益<br>D.流利的口才','A'
union all select '入户拜访的6步骤中属于第1步的是？','A.持续关怀<br>B.预约沟通<br>C.事先准备<br>D.提高粘度','C'
union all select '华北营养顾问林立娜(入职8个月，坚持会员回访，月均回访率45%，7月袋鼠360增长奖金840元)分享：“耕耘就有收获，付出就有回报。”请问如何做好顾客回访？','A.回访前的知识准备<br>B.回访前的顾客名单整理<br>C.真诚<br>D.坚持做','ABCD'
union all select '“我是重庆营养顾问余丽红，热爱自己的工作，真心对待自己的客户，有付出就会有收获。我会认真记录每一个客户的基本信息，与客户经常保持联系，聊聊天，唠唠家常，关心客户产品使用情况，随时为客户排忧解难，让客户体会到关爱。同时也要第一时间将圣元奶粉打折信息通知客户，让客户尽享圣元产品的优惠。这些年，我用真心留住了老客户，又不断收获了新客户，与很多客户成了好朋友，也带动了自己销售业绩的增长。”你觉得这位营养顾问或她的说法哪里值得我们学习？','A.真心对待自己的客户，有付出就会有收获<br>B.与客户经常保持联系，聊聊天，唠唠家常<br>C.随时为客户排忧解难<br>D.与很多客户成了好朋友','ABCD'
union all select '华北营养顾问周洪双（入职十年来，周洪双用微笑面对每位顾客，运用所学育儿知识为顾客提供服务；用实际行动诠释“专业、关爱、可信赖”）分享：“我进入圣元将近10个年头了，这一路走来，付出了很多，成长了很多，同时收获了更多！多拿奖金秘籍：用心服务，珍惜每一个会员，不放弃任何一个机会。”以下说法正确的是？','A.只要学习，就能卖出货<br>B.多拿奖金秘籍：用心服务，珍惜每一个会员，不放弃任何一个机会<br>C.应该用微笑面对每位顾客<br>D.应该运用所学育儿知识为顾客提供服务','BCD'
union all select '“我是厦门刘继红，担任卖场促销组长后，我了解到沃尔玛每年每个厂家都要派人去进行年度大盘点，一去就要一个月，不能在卖场上班，我正在考虑该怎么办，这时卖场主管，让我这个促销组长来安排这个月的盘点人员排期，真是想什么就来什么，可把我高兴坏了，我利用促销员的上班时间差来安排，跟各个厂家的人员分别沟通与商量，最终顺利完成这项工作，大家对我的安排非常满意，并且还使自己避免了盘点工作。”以下说法正确的是？','A.和店方管理人员处理好关系，更容易获得店方资源<br>B.这位营养顾问取得卖场的信任值得我们学习<br>C.和店方管理人员处理好关系可以更快了解店内动向<br>D.和店方管理人员处理好关系会使人际关系更好','ABCD'
union all select '圣元的企业使命是：关爱中国婴幼儿的健康，专注提供优质的产品和服务，为妈妈、宝宝带来健康和快乐。圣元员工的做事原则是人人用心，人人卖力；','A.正确<br>B.错误','A'
union all select '掌中宝是公司给顾问开发的消费者服务管理平台，是非常强大的系统，对顾问更好的服务消费者意义重大，是未来实现直销的重要依托，是虚拟的会员之家。顾问通过掌中宝的使用可以提高对会员的管理效率，提升服务质量，提升会员活跃。掌中宝主要分为四个部分：会员服务、工作管理、微客服、个人中心。掌中宝的功能有会员储存、积分服务、会员沟通、知识学习等。','A.正确<br>B.错误','A'
union all select '客户购买后，在一周之内打第一次回访电话。','A.正确<br>B.错误','B'
union all select '客户问营养顾问小王：“飞鹤奶粉怎么样？”小王说：“飞鹤奶粉质量最差了——”，她这样说对吗？','A.正确<br>B.错误','B'
union all select '“我是安滑片区的张美丽，这一年，公司对营养顾问会员的考核使我感受到了：只要用心做好售后服务，及时回访，急客户之所急，解客户之所优，全心为客户解决好育儿问题，就能取得信任与成功。把客户当家人，将心比心，相信客户也会把你当亲人或朋友，你对客户的付出真情，赢得的是你亲如一家的客情，有了这样的客情，还怕你没有客户，还怕你失去客户吗？客户也会为你介绍客户，这个滚雪球式增加客源，你的销售将是一个什么概念。大家说对吗？','A.正确<br>B.错误','A'
union all select '在掌中宝中给会员发送短信：点击主界面“+”-发送短信-选择会员-点击左下角“+”-选择对应短信-点击短信发送','A.正确<br>B.错误','A'
union all select '标准销售动作主要是为了指导新顾问销售思路。一般标准的销售动作包含①接近顾客；②了解需求；③介绍产品；④处理异议；⑤促单成交；⑥关联销售；⑦相关服务。请问以下哪一步不是标准的销售动作？','A.助销促销<br>B.介绍产品<br>C.接近顾客<br>D.关联销售','A'
union all select '当消费者有了购买欲望，你用了几种促单成交的方法。促单成交的方法有：直接成交法、假设成交法、(______)、(______)。','A.动作辅助法、催促成交法<br>B.赠品辅助法、机会成交法<br>C.动作辅助法、机会成交法<br>D.动作辅助法、否定成交法','C'
union all select '新顾客第一次购买了一听奶粉，在24小时内我们需要发送什么短信？','A.产品<br>B.育儿<br>C.冲调、转奶','C'
union all select '迅速达成销售的技巧有(______)，帮客户确定适合的产品，(______)。','A.缩小客户的选择范围；催促尽快交款<br>B.利益点讲的越多越好；提醒尽快交款<br>C.缩小客户的选择范围；引导尽快交款','C'
union all select '他牌客户来买奶粉，竞品导购没在，你留取客户电话、地址后，准备在入户与顾客沟通，入户拜访的6步骤是什么？','A.①事先准备；②预约沟通；③初次谋面；
④持续关怀；⑤适时销售；⑥提高粘度；<br>B.①预约沟通；②事先准备；③初次谋面；
④持续关怀；⑤提高粘度；⑥适时销售；<br>C.①事先准备；②预约沟通；③持续关怀；④初次谋面；
⑤提高粘度；⑥适时销售；<br>D.①预约沟通；②事先准备；③初次谋面；
④持续关怀；⑤适时销售；⑥提高粘度；','A'
union all select '顾客来买奶粉，说：“价格有点贵啊”，这时候您应该向顾客介绍的利益点主要有产品利益、企业利益和(______)，主要是(______)。','A.差别利益；差别利益<br>B.积分利益；产品利益<br>C.赠品利益；企业利益<br>D.便捷利益；便捷利益','A'
union all select '针对不同的客户，面对不同的问题，我们一般会采取以下哪些介绍产品的方法？','A.FABE法<br>B.竞品对比法<br>C.促销品法<br>D.顾客参与法','ABD'
union all select '如何与转牌顾客互动','A.入户沟通<br>B.每月一条育儿短信，每季度发一条产品卖点短信<br>C.与竞品对比（①不与顾客争论价格，而与顾客讨论价值；
②强调产品价值给消费者带来的利益和好处；
③强调产品与低价竞品对比的优势；）<br>D.电话持续跟进关怀','ABCD'
union all select '掌中宝“会员管理”中“潜在会员”可以通过哪些内容进行筛选？','A.系统分配<br>B.自主添加<br>C.母乳客户、竞品客户<br>D.孕期客户','ABCD'
union all select '顾客说：“我家宝宝一直喝**牌子奶粉（它牌），大便有点发黑，想换个牌子。”请问您该如何作答？','A.关心宝宝情况<br>B.分析常见原因（辅食、药物、铁剂吸收不好也会引起大便发黑）<br>C.给出建议；（宝宝体内火旺，多喝水就会缓解）<br>D.视情况推荐圣元对应系列产品、促单成交','ABCD'
union all select '客户购买后基础服务短信就是每周发送一条回访短信。','A.正确<br>B.错误','B'
union all select '圣元优博产品，仿生配方，是最接近母乳的奶粉，这是圣元优博与其他竞品的差别利益。','A.正确<br>B.错误','A'
union all select '跟进了很久的客户一直没有购买，总是说已经买了。这说明你给客户的印象不是很糟糕，他能够告诉你是个很好的事情。你可以找一个切入的机会，你可以去和客户谈谈什么，看看原因。如果今天不行，没事，继续维护服务便是。','A.正确<br>B.错误','A'
union all select '在掌中宝中查看自己工作成绩：主界面-工作管理-我的成绩','A.正确<br>B.错误','A'
union all select '（会员数量与销量的计算）您的顾客平均每人每月消费500元，您目前有150位顾客，月销量是7.5万元。如果您希望月销量达到10万元的话，您的顾客数量应该有多少？','A.200位<br>B.160位<br>C.180位<br>D.220位','A'
union all select '对于首次购买的新客，我们最晚要做到在多久完成首次电话回访？','A.1天内<br>B.3天后<br>C.3天内<br>D.一星期','C'
union all select '介绍产品的FABE法中E代表(______)','A.优点<br>B.利益<br>C.
特点<br>D.证据','D'
union all select '“我是华北营养顾问杨岚，我越来越喜欢“床旁”，喜欢上这份爱心工作，我们不仅仅是销售奶粉，更是为妈妈宝宝们带去育儿指导和服务！刚接手门店时，我的会员只有5个，到现在掌中宝会员155个，上个月360奖金2170元，和许多姐妹们比起来并不多，但我相信，通过我的坚持和服务，我一定会挣到更多的钱！”你觉得这位营养顾问哪里值得我们学习？','A.我们不仅仅是销售奶粉，更是为妈妈宝宝们带去育儿指导和服务<br>B.服务<br>C.有爱心<br>D.积极','ABCD'
union all select '为下一步和顾客互动，服务好顾客，顾客第一次购买奶粉后，我们需要做：①留取客户资料（家长姓名、宝宝姓名、宝宝出生日期、母亲电话、地址、购买产品，预计下次购买时间等），维护掌中宝；②次日回访使用情况，帮助解决问题；③发送服务短信；④邀约下次购买时间。顾问今天在卖场成功转化一位伊利消费者，在消费者购买后，顾问都应该做哪些工作呢？','A.留取客户资料<br>B.次日回访使用情况，帮助解决问题<br>C.发送服务短信<br>D.邀约下次购买时间','ABCD'
union all select '亲子活动结束后，一位妈妈对营养顾问说：“你们这个活动真好，我也想买奶粉让我宝宝喝，但我以前怎么没有听说过圣元这个牌子呀？”请问您该怎样回答？','A.对圣元优势进行讲解<br>B.您可能对奶粉行业还不太了解，这样我为您介绍一下，圣元是第一家在美国上市的中国食品企业，专业做婴幼儿奶粉及米粉等的企业<br>C.我们的产品比比您就知道，无论营养素的数量和含量上都是最优的，而我们的产品价格也是比较低的，这也是我们把打广告的钱，省下来放到了产品的品质上，您说您买哪个更合算呢<br>D.圣元奶粉也是这家超市卖的特别好的奶粉，您看看这是来我这里购买奶粉的客户，都在这本上记着呢（拿出客户资料本）。您是哪的？您看某某，就是您们那里的。他家宝宝从出生一直喝','ABCD'
union all select '入户拜访时，顾客说她们家的宝宝就是不爱喝白开水，请问您该如何帮助解决？','A.理解<br>B.强调喝水的好处；（正常发育，避免上火等）<br>C.解决方法；（耐心引导、调整喂养工具、调整口味如少量稀释的果汁、奶粉等，妈妈要多喝水，营造喝水的气氛等）<br>D.其他表现（自然、大方、自信、亲和、微笑等）','ABCD'
union all select '顾客来到店里找他牌奶粉，如何与这位顾客沟通?','A.关心宝宝情况，并抓住顾客需求；根据需求，对比竞品介绍产品<br>B.选择更加适合宝宝的
①不贬低对手；
②拿自己的优势与对手的弱点做客观地比较；
③强调自身的独特卖点。<br>C.举实例使顾客放心（主席签约照片、央视新闻照片等）<br>D.介绍转奶方法，安全放心','ABCD'
union all select '顾客由单品购买变成多品种购买不能提升销量。','A.正确<br>B.错误','B'
union all select '如果客户下过单，那么总有一个地方有打动过他。为什么当初合作了而现在没有了？你可以引导客户去回复，让客户说出来。了解客户的需求，他可以不购买，但你要通过互动去了解。','A.正确<br>B.错误','A'
union all select '在掌中宝中给会员打电话：点击主界面“+”-打电话-选择会员-拨通','A.正确<br>B.错误','A'
union all select '一位会员有8个月购买过优博，她属于？','A.A类会员<br>B.B类会员<br>C.C类会员<br>D.D类会员','B'
union all select '向竞品顾客介绍的产品功能好处时，需要介绍的利益点主要有①产品利益，即产品带给顾客的利益。②企业利益，由企业的技术、实力、信誉、服务等带给顾客的利益。③差别利益，即竞争对手所不能提供的利益，也就是产品的独特卖点。营养顾问拦截了一位飞鹤消费者，顾问应该从哪几个利益点进行介绍呢？','A.对比利益<br>B.产品利益<br>C.企业利益<br>D.差别利益','BCD'
union all select '了解顾客需求，针对需求介绍产品是销售成功的关键。那么想了解顾客需求，可以通过哪些问题来实现？','A.现在吃什么<br>B.谁使用、有什么问题<br>C.以前用什么<br>D.需求什么','BCD'
union all select '“我是深圳营养顾问黄梦梅，深圳一区的姐妹知道，有投诉找梅姐，做为一名营养顾问，心中必须有专业和爱，对会员有求必答。我09年加入圣元，通过几场培训，我对自己说我是名营养顾问，并不是仅仅一名卖奶粉的促销员，一般的促销员怎么可能懂这么多。所以平时坚持做最喜欢的两件事：第一：真心和客人沟通；第二：用心上门服务。所以在时间的积累下，慢慢的我成为这座移民城市外来劳务人员中最可信赖的梅姐。所以我收获着也快乐着。”你觉得这位营养顾问的说法正确的是？','A.做为一名营养顾问，心中必须有专业和爱，对会员有求必答<br>B.我们是名营养顾问，并不是仅仅一名促销员，一般的促销员怎么可能懂这么多<br>C.真心和客人沟通<br>D.用心上门服务','ABCD'
union all select 'FABE法：通过介绍产品特征转化为顾客利益的销售方法；F代表：优点；A代表：特点；B代表：利益；E代表：证据。','A.正确<br>B.错误','B'
union all select '在掌中宝中帮会员积分：点击主界面“+”-会员积分-可搜索会员-选择会员-添加积分-扫积分码或输入积分码-确定','A.正确<br>B.错误','A'
union all select '会员手机换号了，处理办法：打金币联盟4000188180电话变更新手机号，掌中宝不做任何变动，第二天同步掌中宝','A.正确<br>B.错误','A'
union all select '聪聪妈妈是在2月份、5月份、8月份购买过产品，活跃的月数是3，她属于?','A.A类会员<br>B.B类会员<br>C.D类会员<br>D.C类会员','D'
union all select '快成交时，你跟一位新客说：“您是拿两听还是三听？”这是什么成交法?','A.直接成交法<br>B.动作辅助法<br>C.假设成交法<br>D.机会成交法','C'
union all select '若使老消费者延续购买，你需要做？','A.客户购买后基础服务短信：每月一条育儿短信，每季度发一条产品卖点短信<br>B.定期对老客户进行梳理；定期的回访；保持持续的热情，像新客一样对待<br>C.持续关怀，定期服务，生日或节日时问候<br>D.用心服务是获取优质会员的保障
用心服务是提升会员数量的唯一法宝','ABCD'
union all select '正确、自然的接近客户是了解需求和介绍产品的前提。你认为以下哪些方法是接近消费者的技巧？','A.握手<br>B.打招呼<br>C.介绍商品<br>D.赞美','BCD'
union all select '客户在奶粉通道寻找奶粉的时候，不是接近客户介绍产品的好时机。','A.正确<br>B.错误','B'
union all select '在掌中宝中帮会员兑换礼品：点击主界面“+”-兑换礼品-可搜索会员-选择会员-选择礼品-兑换-添加具体地址兑换','A.正确<br>B.错误','A'
union all select '“我是华西营养顾问杨晓红，老顾客宝宝大了不吃奶粉了或者转吃其他了，我不轻易放弃，经常联系，现在二胎政策放开，很多家庭迎来了二胎宝宝，老顾客又可以购买婴幼儿奶粉了。坚持和老顾客联系，维护好这些来之不易的老顾客。我相信我做好会员互动，把顾客当成朋友，坚持下去，这条路一定行得通，我们每天的努力和付出总会有回报的。我们要在平时的工作中不断学习、提升自己的专业知识和技能，才能更好的服务宝宝。”你觉得她说的对吗？','A.正确<br>B.错误','A'
union all select '电访的过程中，发现一位老客户因为促销活动的原因，转成了他牌客户。为了宝宝继续食用优博奶粉，你需要把优博奶粉与他牌进行比较。那么，如何与他牌比较呢？','A.拿对手的优势与自己的弱点做客观地比较<br>B.不贬低对手
<br>C.强调自身的独特卖点<br>D.贬低对手','BC'
union all select '掌中宝中“工作管理”-“工作提醒”包含哪些内容？','A.生日提醒<br>B.预产期提醒<br>C.新客户服务提醒<br>D.沟通提醒、延续提醒（购买提醒）','ABCD'
union all select '掌中宝中“工作管理”-“我的成绩”分为哪些内容？','A.业务数据<br>B.我的收获<br>C.我的荣誉','ABC'
union all select '在货架前，正对竞品可以更好的拦截客户','A.正确<br>B.错误','B'
union all select '在掌中宝中添加会员：点击主界面“+”-添加会员-输入会员信息-点击“确定”','A.正确<br>B.错误','A'
union all select '“我是华北营养顾问杨岚，我想和大家分享的是：等销售是等不来的，机会只能自己多多争取，床旁和电访坚持下去就是生产力！顾客拒绝一次两次三次，都没关系，我们缓缓，再来一次；再争取一次，说不定下次就真的成了呢！不怕拒绝就会变得很强大。很多时候你做的工作，一时半会见不到成效，但是你要知道春耕秋收，耕耘和收获原本就不是一个季节。当你迷茫时不要怕，你不是没有成长，而是在扎根。”以下说法错误的是？','A.等销售是等不来的<br>B.机会只能自己多多争取<br>C.不怕拒绝会变得很强大<br>D.每个人都必须去做床旁','D'
union all select '“我是天津营养顾问谢彦荣，以诚相待！将心比心，必将换来顾客的以诚相待！顾客的需求就是我服务的方向！加油自己，加油亲爱的姐妹！随着法版优博的上市2017希望越来越好！”你觉得这位营养顾问哪里值得我们学习？','A.真诚<br>B.服务<br>C.付出<br>D.真心','ABCD'
union all select '你本月的销售目标增长了10%，要达成目标销量可以从多个方面入手的，以下哪些方法可以提高销量？','A.由一次购买变成多次购买
<br>B.由小额购买变成大额购买<br>C.由单品购买变成多品种购买<br>D.由单个顾客变成群体顾客','ABCD'
union all select '“宝宝的健康最重要了，您说对吗？”“您知道什么营养对宝宝的智力发育最好吗？”“您的宝宝是顺产的还是剖腹产的呢？”都属于封闭式的问题。','A.正确<br>B.错误','B'
union all select '在掌中宝中进行“会员管理”：主界面-会员服务-会员管理','A.正确<br>B.错误','A'
union all select '这款奶粉含有高含量的藻油DHA，它可以促进宝宝大脑发育，让您的宝宝更加聪明，您看我们这里很多宝宝都在用。用(______)标准句式描述奶粉中DHA？','A.FAE<br>B.差别利益<br>C.产品利益<br>D.FABE','D'
union all select '实际销售过程中，最让顾客信任的是什么？','A.营养顾问、品牌、门店<br>B.营养顾问、品牌、促销品<br>C.营养顾问、专业知识、促销品<br>D.摆台活动，促销品、门店','A'
union all select '“我是营养顾问琴姐，有一次，一个顾客来买奶粉，店里确缺货，我和顾客商量了半天，可是顾客家中已经没有一点奶粉了，要是我们没有，那就要换奶粉了。在这种情况下，马上求助我们的商务经理，商务经理立即送货过来。当时我很感动，因为经理离我们的店有二十几公里。现在这个客户家的宝宝都两岁多了。还在吃我们的奶粉，还是我的忠实客户，给我介绍了几个新客户。”以下说法正确的是？','A.这个案例说明库存不重要<br>B.这位顾问值得学习的地方是抓住顾客<br>C.好的库存的管理标准是“产品出货能做到先进先出、有安全库存意识，能提前预警缺货，并提醒销售人员下单”<br>D.应保证合理库存，不出现断货、缺货和180产品','BCD'
union all select '要想博得新顾客好感：①给客户良好的外观印象；②注意客户的情绪（多讲客户感兴趣的话题）；③先入为主的暗示效果；④要记住并经常说出客户的名字；⑤让你的客户有优越感；⑥替客户解决问题；⑦利用小赠品来获取客户的好感。以下说法正确的是？','A.找到顾客的需求，为顾客解决问题可以博得新顾客好感<br>B.学会倾听，让顾客信赖可以博得新顾客好感<br>C.获得帮助、解决困难可以博得新顾客好感<br>D.做好售后服务可以博得新顾客好感','ABCD'
union all select '（会员数量与销量的计算）顾客平均每人每月消费500元，您由原来的100位顾客增长到现在的120位顾客。以下说法正确的是？','A.您原来的月销量6万元<br>B.您原来的月销量5万元<br>C.您现在的月销量6万元<br>D.您现在的月销量5万元','BC'
union all select '“我是云南营养顾问杨小丽，之所以我能和顾客是朋友，是因为我对我们的产品很自信，这份自信能让顾客信任你，如果产品经不起考验，我自己没有信心，那我说得天花乱坠也没用。这产品不仅让我成为了顾客的朋友，也让顾客成为了圣元奶粉的见证人，使我们的产品更具有说服力，也让我们的市场越来越大，道路越来越宽，朋友也越来越多。”你觉得她说的对么？','A.正确<br>B.错误','A'
union all select '圣元的企业使命是：关爱中国婴幼儿的健康，专注提供优质的产品和服务，为妈妈、宝宝带来健康和快乐。','A.正确<br>B.错误','A'
union all select '掌中宝可以为任何消费者积分，点击主界面“+”-会员积分-输入手机号-添加积分','A.正确<br>B.错误','A'
;