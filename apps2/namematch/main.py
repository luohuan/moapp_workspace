#from moapp.server.globals import user, app, page, mo, params
#coding=utf-8
import logging
import sys
import os
import traceback
from sys import path

import random
from calc import *
# 入口函数，在这里声明MoApp，定义页面

DESCRIBE = [
    '在你们的友情里，有一方比较强势，有一方比较弱势。强势的一方对自己有明确的定位，喜欢惹人注目，受人崇拜；而弱势的一方则较为柔和，即使也充满了热情，但是却更喜欢低调一些。你们有时候会因为性格而发生矛盾，但是这些矛盾在你们似火的热情下不值一提。只要能够更多地考虑对方的感受，那么可能就会获得更多的温暖和动力。',
    '你们两个人都充满了激情和火热，很容易就可以感受到对方的激情。所以一旦相遇，友情的小火苗回立刻点燃，一拍即合。认识早的话，很可能成为死党，认识晚的话，也可能成为知己。',
    '你们一个踏实可靠，一个激情似火，看似性格上有一些不同，实际上却很互补，会相互包容对方的缺点。正因为包容，所以你们做事的理念、节奏会很合拍，天生适合做彼此志同道合的朋友。',
    '你们中的一方会比较善变，就像拥有双重人格，另一方则热情似火，能够应这种突如其来的变化，维持一份很美丽的友谊。虽然大部分时候会比较合拍，但是有时也会难以应付对方，相处起来可能会觉得有点累。',
    '你们有一方会比较内向、怕羞，不容易相信别人，但另一方往往激情多，耐性少，不善于应付起伏不定，是需要强烈安全感的人。相处起来可能会有一些小摩擦，但是在患难的时候，倒是可能成为帮对方一把的人。',
    '你们一方面性情相近，都是急性子的人，可以说是一拍即合，但是当你俩都很有想法，遇到意见不一致时，可能会产生磨擦，但有不同的声音，才能督促彼此共同进步。',
    '其实从性格上来说，你们不是同一类人。其中一个人比较踏实保守，凡事追求完美，是个超级挑剔家；而另一个人则比较冲动，经常被对方气得火冒三丈。但是，当自己真的犯错误的时候，对方可能会给你正确的批评和帮助。',
    '你们有一个人喜爱追求自由，但是同时也需要通过展示实力来获得肯定，有很好的交际能力，在友情中扮演包容和调解的角色。而另一个人则热情似火，会非常热情地欣赏对方的能力。所以你们呆在一起，双方面都得到平衡，互补长短，相得益彰。',
    '在你们两个人当中，有一个人警惕性更强，会没有安全感，很难以信任别人，但是只要认定了另一个人，就会对对方这个朋友死心塌地，成为不计较名利，坦诚相待的朋友。而另一个人则会比较热情主动，所以你们的相遇，将会促成一段最美丽的友情。',
    '你们当中有一方会扮演持续输出热情的角色，这一方会性急、热情，而另一个人则喜欢浪迹天涯、随遇而安，所以你们可能不常见面、聊天，但当你们迷茫时，对方的启发或许能给你柳暗花明的感觉。',
    '在你们的交往中，相对热情的一方会特别另一方脚踏实地，理性隐健的作风，所以你们彼此互相欣赏，在逆境中拼搏时，对方能给你们带来了坚持到底的勇气，构成的友情也会非常地坚固。',
    '你们的友情中充满了缘分，就如水和植物的关系，所以你们会发现遇见彼此，是最美丽的意外，是你伤心时的依靠，是你高兴时与你分享快乐的人。',
    '你们的性格看起来可能并不一样，但是一个会多愁善感和另一个则热情似火，充满了相互吸引的潜质，所以实际上最可能成为懂得欣赏你的知音人。你们在生后中将会成为彼此最合拍的拍档。',
    '你们两个人对生活的稳定和界限有超出常人的追求，所以只要相遇成为朋友，那么友情会稳定到极致。你们品性相投，无需刻意保持距离，计算尺度，只需素面朝天，就能通晓对方的心意，如果说真的有什么不足的话，那可能就是会缺少一点奇思妙想上的调剂吧。',
    '对于你们来说，一个人会偏向踏实稳重，另一个人则会追求自由，聪敏灵活，性格多样化。在短时间呢，你们虽然吸引，但捉摸不定，你们的友情仅止于认识的阶段，连普通话题也未必有机会聊上。',  
    '从性格上来说，你们俩有很多的共同点，都会追求稳重踏实和安定善良目标，同时也非常热爱家庭生活，所以你们能相处的很融洽。',
    '不管是性格还是追求，你们的都惊人地一致，都拥有强大的专注力、持久力、执著力，所以会始终如一地勤奋好学，毅力惊人，不达目标誓不罢休，当你们相遇的之后，一定会成为共学、共道的朋友。',
    '作为朋友，你们的性格非常地合拍，内心都拥有保守而踏实的本质，理性多过感性。所以你们相处时也许有些乏味，但双方都绝对信任对方，属于可以共患难的朋友。',
    '你们的性格其实略有不同，但是并不会产生矛盾，反而会互相弥补。你们彼此之间无拘无束和保守踏实的特点刚好互补。你们未必可倾诉心事，但是因为对彼此的友情有特殊的执着，所以往往都可以互相帮、互相照顾。',
    '你们两人最大的共同点就是拥有深情和忠诚的本性。在相处当中，相对踏实的一方会照顾相对浪漫的一方，可以说是很合衬的朋友。因为同样看重忠诚和深情，所以你们的友情可以经受共患难，同富贵的考验。 ',
    '从性格上来，你们的差异可能还挺大的：一个人会更漫不经心，随遇而安，对生活没有太大的追求，但是另一个人充满了执行力和感染力，所以往往可以帮助前者增长见识，开拓思维。所以你们的友情会让彼此感到非常地舒适，收获很多的知识。',
    '你们共同的优点就是踏实靠谱、务实稳重，所以构成的友情会像大地一样异常地坚固，虽然可能会缺少一些乐趣，但是你们作为实际主义者，不会天天寒暄，却会雪中送炭，不会日日问候，却会济困解危。',
    '你们的性格有一定的差异，但是却可以相互弥补缺点。其中一方会拥有超出其他人的执行力和目标感，而另一方追求自由和无拘无束。所以性格上的差异，让你们难得有非常一致的共同意见，但是如果抱着学习的心态，却刚好可以取长补短，相得益彰。',
    '在你们的友情当中，有一个人会像水一样温柔和善，总能包容朋友的缺点，而另一个人恰好在内心又渴求安全感。你们都喜欢尝试新鲜的事物，所以时不时会有一些冲动的想法，一起屁颠屁颠地去实现。所以，如果可以保持沟通，相互理解，你们的友情可能会非常长久。',
    '不管是性格还是爱好都惊人地一致，所以对彼此的性格都了若指掌，你们都喜欢四处追寻自由，都喜欢追求新鲜刺激，成为朋友的你们，就如同左手和右手一样和谐。不管是成功还是失败，不管是高兴还是伤心，总能在第一时间体会到对方的感受，成为对方内心深处最信任的那个朋友。',
    '在你们的交往当中，弱势的一方会极度缺乏安全感，所以在友情中会体现比较强的占有欲，他们会想要获得对方更多的关注，而强势的一方则更喜欢自由，追求新鲜刺激。虽然在性格上可能会有一些不合拍，但如果彼此能多给对方一些自由，那么你们将会变得更优秀，从而获得最独特的友情。',
    '在你们两人当中，总有一个人充满了热情，充满了持续输出的活力，因此时时刻刻都拥有显眼的光芒，总能成为人群中的核心，与生俱来的热情与活力，可以让对方感受到春天阳光般的温暖。而另一个人恰好可以理解、促进对方的火焰。所以你们就像彼此生命中的那道不可缺少的光，成为最亲密无间的朋友。',
    '你们中的一个人心思细腻敏感，总希望得到朋友更多的关注和呵护，也许会给朋友带来一些压力。另一个人则温柔和善，总能在第一时间发现对方的小心思，在最合适的时候温暖彼此。所以，你们的友情不一定会像太阳一样耀眼，但是却可能像春风一样舒适。',
    '你们的性格非常地接近，所以简直可以称得上是知己。在追求自由的时候，善于理解对方的含义。所以你们都很好动，都喜欢体验新鲜的事物，在很多事情上都能步调一致。很多时候，要说的话只说了一半，对方可能就理解你的想法了。你们友情中充满了和谐和默契，更充满了轻松和愉快。',
    '成为朋友的你们会彼此互补对方的不足。一个人喜欢追求自由，所以喜欢寻找新鲜的事物。而另一个人则会更加执着，更怀念过往的记忆。虽然有时候你们会有争吵，但是一旦成为朋友，你们可能就会聪明地吸收对方的优点，在友情中彼此学习，彼此成长，相互鼓励越过挫折，翻过障碍。',
    '你们会成为互相影响最深、吸引力的朋友。你们都拥有热爱自由、都有旺盛的求知欲望。一个人为人乐观包容，另一个人则浪漫有趣，在一起的时候你们总能快速地发现生活里的新鲜事。所以，你们一路走来，友情的道路上可能充满了美丽的景色。',
    '在你们的友情里，你们有一个人会更开朗活泼，喜欢追逐新鲜的事物，而另一个人在坚强的外表下，却有一丝害羞的心结。在外人看来，你们的性格不大合适，但是实际上，你们只要能够多理解对方，多包容对方，给对方留出更多的空间。那么，你们很有可能会收获一个能让自己变得更优秀的朋友。',
    '因为性格相似，所以你们在心灵上很容易产生共识共鸣。不过，因为你们都喜欢追求自由寻找新鲜，所以如果想要维持友情的长久，一定要让对方看到你内心的感情，而当你们真正走进对方的内心，可能会发现彼此原来是那么地相似。',
    '作为朋友，你们有着很多的共同点，最大的特质就是追求变动和自由。其中一个人会多情、浪漫、博爱，希望能多出去玩、多感受这个世界。而另一个人则纯真、温柔，希望朋友能够给自己更多的依靠。看起来有那么一点不合拍，但是实际上，只要能多去倾听对方的感受，就会一起变得更可靠成熟，更独立坚强。友情可能也会因为理解，变得更亲密。',
    '你们几乎拥有相同的缺点和的优点，总的来说就有着极强的感受力，所以总能在第一时间感受到对方的喜怒哀乐，和对方一起开心，一起难过。有时候，甚至一个眼神就能抓住对方内心的想法。所以，成为朋友的你们，将会是彼此在情感上最大的依靠。',
    '你们在一起的时候，总有一方会扮演火焰的角色——热情强势，而另一方则扮演水的角色——敏感细腻。因为水和火本质是矛盾，所以在你们的友情道路上，总免不了一些磕磕碰碰。当你们学会理解对方，学会包容对方，那么这些小矛盾可能会像一个个考验，让你们的友情变得更加坚固。',
    '在相处交往的过程里，其中一个人会追求稳定的友情，而另一个人虽然看起来流动无常，但是实际上适应能力非常强。所以你们有很多的共同点，对待朋友都会无比的忠诚可靠，不会做出伤害对方的事情。但是因为性格上的差异，总是免不了会有些小摩擦。但是这只不过是友情的点缀，当学会换位思考，可能会发现对方是自己一直等待的那个好朋友。',
    '你们最大的优点就是能够非常稳定地输出感染力和执行力，总能够不停地适应和磨合，所以往往能让友情充满激情。也许过度地追求自由和洒脱，会不停地吵吵闹闹，但那只是友情的调剂，前一秒钟还互不相让，后一秒钟就会笑成一团。外人不能理解，但是你们却乐在其中。',
    '在这段友情里，你们都像流水一样很容易情绪化，同时还拥有高度的直觉和心灵感应的能力。很多时候，只有你们才能理解、包容对方突如其来的小情绪。在对方最无助的时候，成为可以依靠的那个人；在对方最开心的时候，成为可以分享的那个人。',
    '在友情开始之后，你们中的一个人会开朗外向，有广阔的胸襟和视野，有浪迹天涯的愿望，而另一个人则随遇而安，看起来水和火毫不相容，但是却都会包容彼此的不足，可以有效地弥合二者的矛盾。你们可能陪伴彼此的机会不多，但是在内心却渴望成为对方那样的人，相互之间会产生强烈的吸引力，从对方的眼中看到不一样的风景。',
    '你们的世界看起来距离有点远，但是距离恰好会产生美，所以又会互相吸引，互相影响。要走近对方并不难，热情的一方可以点燃另一方隐藏的激情和冲动，虽然少不了要磨合沟通，但是只要你们友情的火焰被点燃，那么可能就会越烧越旺，给彼此带来光和热。',
    '你们两人的友情观其实会有一点差异，一个追求自由洒脱，另一个追求稳定，看起来有一些背道而驰，但是却是最好的互补。你们会带彼此去看远远处的风景，会成为彼此停靠的港湾。你们的友情，可以让对方获得更多的依赖，相处的时间不多，但是却永不会褪色。',
    '你们都是最浪漫的人，柔情似水，温馨感人，在其他人看来，你们就是天生的朋友。两个人都非常善于适应和理解，所以你们的友情里没有争吵，更没有冲突，有的是最细腻的体贴，最温馨的陪伴。如果你们足够细心，可能会发现身边到处都是嫉妒的目光，因为巨蟹和双鱼的友情真的是太可贵了。',
    '你们都是那种大大咧咧的人，充满热情，直来直去。而且，不仅有满满的热情，而且还能持续释放活力，所以会是最强势，最热烈的一对朋友。最开始可能会争强好胜，但是很快就会惺惺相惜，因为只有对方可以和自己势均力敌，只有对方才能和自己打个平手。所以，成为朋友的你们，会一起迎接挑战，会一起变得更强大。',
    '因为性格的差异，在你们的友情里，少不了会有一些吵闹。但是，好朋友本来就不只是会夸你，有时候也会批评你，但是他们并不是讨厌你，而是想让你变得更优秀。所以，如果对方愿意指出你的错误，那是希望你不停地进步，你可一定要珍惜呀。',
    '你们在热情和自由上拥有非常强的共同之处。所以你们的性格会非常地相似，都是那种热情似火的人，很容易就会成为朋友。你们会快速地从对方身上找到美感，发现对方的优点。在一起的时候，总会觉得自己是天底下最优秀的那个人。在对方的鼓励之下，你们的干劲会越来越足，也会变得越来越优秀。',
    '在你们的友情里，有一方比较强势，有一方比较弱势。强势的一方对自己有明确的定位，喜欢惹人注目，受人崇拜；而弱势的一方则较为柔和，即使也充满了热情，但是却更喜欢低调一些。你们有时候会因为性格而发生矛盾，但是这些矛盾在你们似火的热情下不值一提。只要能够更多地考虑对方的感受，那么可能就会获得更多的温暖和动力。',
    '在友情当中，你们中的一个人更喜欢成为世界的中心，同时表演欲望也很强，总想在人群中获得别人的关注。但是另一方则热爱自由，并不是那么容易感受到对方的热情。一旦在茫茫人群中认识到对方的价值和可贵之处，友情的小火苗可能就会一发不可收拾。毕竟，有了好观众，好演员才有价值。',
    '你们的性格有一些不同，有一个人会更看重实际，而另一个人则充满了热情的幻想，在刚认识的时候，你们可能并不会马上成为好朋友。但是相处越久，就会被彼此的浪漫和踏实所感染。在日复一日的交往中，你们可能会在不知不觉中，变得越来越优秀。',
    '你们的性格和生活方式离得有点远，但这也是最容易相互吸引的原因。你们的友情就如同天空与大海，也许距离很远，但是却又拥有同样的底色，同样的气质，同样的内涵。',
    '在你们两人当中，有一个人会浪漫、温柔、多情，而另一个人则强势、热情、冲动，看起来不怎么合拍，但是后者的富有主见恰好可以弥补前者的优容寡断，而欠着又能软化后者的强势。虽然你们的友情需要一段时间，但是只要度过了磨合期，可能就会收获一个帮你改掉臭毛病的好朋友。',
    '你们两个人的性格特点都是追求踏实的生活，所以当你们相遇的时候，会获得最坚固的友情。你俩都很凊楚自己的优缺点，只要你们不将注意力集中在对方身上，多 些发掘对方的其他才能好处，双方尽量避免互相挑剔，那么，你们也算得上是一对知己知彼的好伴侣。 ',
    '在你们的友情里，有一方会持续地对身边的人释放友善，因此拥有极强责任感，他不会只顾自己的利益，也会照顾别人的权利，是个公平公正的人，虽然另一方可能会有点苛求完美，但由于前者很会照顾别人的感受，所以反而会彼此体谅对方，也不会产生隔阂，相处起来很惬意、自在。',
    '你们的性格会有一点差异，一个追求浪漫的生活，另一个则向往踏实的僧或，所以不太容易与人达到很深层次的共鸣，有时候会就一些小问题产生矛盾，但是并不能动摇你们友情根基。毕竟对方是一面骂你，一面为你擦眼泪的朋友。',
    '你们当中会有一个人像一团熊熊燃烧的火焰，豁达、开朗、交游广阔，自由自在，而另一个人则会像厚实大地一样，踏实、稳重，绝不胡言乱语。你们一个理性一个感性，所以你们可以说是既互斥又互补的人，有的时候可能会意见相左，但是有的时候也能合作把事情完成的很亮眼。',
    '你们的友情非常地合拍，没有一百分，也有九十八分。其中一方会给朋友非常好地照顾，除了使对方精神愉悦外，还会有物质上的倾囊相助，可算是个忠实可靠的好伙伴。而另一方则细腻坦率，会为朋友着想打算。你们俩都是实用主义者，无论是精神还是物质上，都可以让彼此越来越富有的知心朋友。',
    '你们的性格都很与众不同，其中一个人会追求自由，因此思想前卫，神秘莫测，而另一个人则会追求稳定踏实。在一起的时候，彼此可能不太容易会接受对方的的建议和想法，所以你们是不同世界的人。所以如果想要成为好朋友，一定要多理解包容对方的心。',
    '你们看起来像是两个世界的人，但是通常是最能互相吸引的朋友。其中一个人会爱浪漫、爱幻想，时时表现出柔情蜜意，而另一个人则遇柔即化，所以完全无法抗拒对方的温柔可爱，同时也会被感染。成为彼此的朋友，就是你们最大的幸运。',
    '你们两个人对自由都非常地执着，当你们相遇，很快就会熟知对方的习惯，也明白对方需要的是什么，而且你们都乐于和对方作伴，可以说是心腹之交。即使你们两个都多多少少可能有点优柔寡断，有时候会有一种事情推不开，进展不了的感觉，但是你们能够相互提醒对方，学习当机立断，给彼此鼓励，可以说是最难能可贵的朋友。',
    '虽然你们性格上有一些不同，但是对友情都有天长地久的追求。都会拥有超人的执着和坚定的信心。但是正因为过于执着，反而会有一些疑神疑鬼，所以你们俩如果想让友情更持久，就需要彼此加强信任，对对方的内心加深理解。',
    '在交往的过程中，你们有一方会像风一样热爱自由，所以魅力是与身俱来。而另一方则像火一样四处散发热情。所以严格来说，你们都是魅力四射的人，有讲不完的话题及数不尽的话题。你们往往都有很多的朋友，懂得尊重别人，会理解彼此对自由和热情的追求， 因此你们二位可以算是能相伴相依走天涯的一对好朋友。',
    '你们的性格差距其实是有一点大的。其中一个人会浪漫自由，所以是个注重情趣的人，而另一个人则踏实靠谱，不重情调，甚至内心里对这种小情调嗤之以鼻，无法理解天秤的“享乐”思维和热爱和平的理念。而且你们又都有一些固执，对自己的立场有超常的坚持，所以如果你们想要维护友情，就一定要学会换位思考，多考虑对方的想法。',
    '因为性格非常互补，所以你们两个是比较契合的朋友，其中一个人是沟通专家，而另一个人不善表达自己的感情，当你们相遇之后，前者可以满足自己倾诉的需求，后者可以获得安慰。所以，你们的友情会细水长流，成为滋润彼此无话不谈的好朋友。',
    '你们最大的共同点就是都拥有浪漫情怀，追求自由，温柔适应。所以你们要警惕太过于自由，太过于梦幻，以至于让对方产生不安全感，觉得自己被忽视被冷落。总之，多花一些时间维护好这份友情，会让你们的人生都充满光彩。',
    '你们都拥有超强的适应性和浪漫主义情怀，而且浪漫主义情怀是你们生活的常态。当你们相遇的时候，向心力的能量会让你们都想占有对方，而且你们都有灵敏的直觉，是非常合适的一对，不过要注意的是需要自我克服一些内心的不安，不要怀疑对方的情谊，这可以让你们的友谊永不退色，历久弥香，成为一辈子的挚友。',
    '你们中的一个人会充满热情，而另一个人总能随时配合这种热情。你们的相遇会带来神秘莫测的变化。你们无论在思想上、行为上都喜欢自由自在，天际任纵横没有思想包袱，永远活泼开朗。',
    '你们的性格其实差距有一点大。其中一个人会比较保守内向，所以在生活中并不会呈现出太大的热情，亦没有很浪漫的情结。这些特质可能会让积极热情的一方犹豫不决，因此在情绪上要的很多，比较追求精神上的愉悦，否则就会产生对对方的不信任感。 所以想要维持好这段友情，一定要尝试主动去了解对方。',
    '在交往和友情当中，你们有一方天生就叛逆，思想前卫，无法用传统观念衡量他，思维也天马行空，而另一方则会缺乏安全感，所以很容易转变成占有欲。对于这样的不安全感，前者要给与给多的理解和体贴，后者则要多信任对方。相信你们的友情会更美好。',
    '在你们的友情里，有一方总会是对另一方的魅力沉迷不己，两者相遇注定会充满了罗曼蒂克，你们都可以尽情发挥自己的长处，不过，还是可能要多理解对方和自己不一致的想法，除此之外，你们几乎上是完美的伙伴，能够从彼此身上看到不一样的风采。',
    '你们都会像火焰一样向四周散发自己的热情。当你们相遇，就拥有同样的底色，同样的气质，同样的内涵，一如了解自己般凊楚对方，包括优点还有缺点。如果你们可以多改掉射手座不停改变目标的毛病，彼此能够相互鼓励，改正缺点，发扬优势，你们将会是相互陪伴，探索人生的知心好友。',
    '你们两个人既充满了热情，又非常地重视稳定。一方会热情似火，另一方面则信心满满。所以，如果大家愿意多花时间呆在一起，然后再推心置腹多些耐心，那么将会使你们的友谊发生天翻地覆的提升。',
    '在这段友情里，你们一个人就像风，另一个人就像火，风会促进火的熊熊燃烧，所以你们都有一个高度活跃、发达的心灵，双方惺惺相惜，感情可以维持一短彼长的时间。虽然象征风的一方在性格上会比较叛逆，但为人乐观包容性强的特点则可以增添情趣。 所以，你们在一起碰撞出创新的火花，适合在一起探讨学习。',
    '在你们两个人当中，有一个人会非常喜欢浪漫，总喜欢能够感受到朋友的热情，而另一个人恰好拥有持续不断的浪漫和热情。所以，你们的友情会非常地合拍，再简单普通的约会和活动都会让你们开心得不得了，是天生就注定要成为朋友的人。',
    '你们两个人的性格非常地相似，都可以让性格中稳定踏实的特点发展到极致。你俩都能够了解彼此的需要和感受，都有勤奋上进的决心，或者还拥有共同的人生目标。你们可以不仅精神上可以相互慰藉，学业和事业上都能相互帮助，是难能可贵的相互扶持的好朋友。',
    '从思维方式上来说，你们是有不同点的。其中一方思想活跃，喜欢破旧立新，不受传统束博，而另一方则偏向保守，凡事非常在意计划性。看起来有矛盾，但是实际上具有相互吸引的特质。你们都有着天生的使命感，很想创建一番事业，惠及他人，这点将会是你们友情的基石。',
    '你们能够成为好朋友也是一件挺神奇的事情。其中一个人比较喜欢浪漫的氛围，另一个人则喜欢踏实的生活，都不是彼此心目中的理想朋友，从这个角度来看，你们似乎不太能成为朋友。但是，你们对朋友的接纳度非常地高，很容被对方的温柔和可爱所感染，所以才可以破除自己内心的执念，成为对方不可多得的好朋友。',
    '你们本身就是天马行空的人，脑子里充满了各种奇怪的想法，而且极度追求自由。所以，当你们相遇，就会化身为思想狂徒，那么，两个思想狂徒走在一起，后果会是怎样？碰撞出思想的火花，这样的搭配很有刺激感和新鲜感。在一起有讨论不完的问题有趣而且充实。所以，水瓶遇到水瓶，势必会成为知音。',
    '你们的相遇很容易创作出世界上最浪漫的组合。其中一个人会是世间少有的浪漫家，会带着另一个人四处闲逛。而另一个人也从来不缺少奇思妙想，会配合得天衣无缝。但是自由和浪漫都是需要空间的，如果你们俩已经成为朋友，记得多给彼此空间，那样你们的友谊才会有弹性更长久。',
    '你们最大得共同点就是都对浪漫有超出常人的执着，所以一旦相遇，会让友情的向心力不停地叠加。你们会心灵合一，彼此看透对方的心意，聊起天来总能get到对方的点，思维高度在同一层面，如果能够改掉变动善变的缺点，多给对方一些关注，那么就能够更好的理解和包容彼此，这可以使你们的友谊更长久而且坚固。',
]



NUMBERS = {
    'number1': [
        '数字1代表了神性。',
        '数字1是万物的开始和起源。',
        '数字1代表缘分开始的地方。',
    ],
    'number2': [
        '数字2表达了友情的另外一面，也就是二元性。数字2代表平等和平衡。',
        '数字2代表表示平衡、选择和决定。',
    ],
    'number3': [
        '数字3代表了多样性',
        '数字3代表了生生不息的希望',
    ],
    'number4': [
        '数字4是代表均衡的基础',
        '数字4代表稳定和永久',
    ],
    'number5': [
        '数字5代表了运动，时间和改变。',
        '数字5预示着新的生命力和新的可能性。',
    ],
    'number6': [
        '数字6代表意识的显露和净化',
        '数字6给身心带来整体化的认识，促成和谐',
    ],
    'number7': [
        '数字7代表胜利和荣耀',
        '数字7是一个神圣的数字',
        '数字7代表了开始和唤醒的状态',
    ],
    'number8': [
        '数字8是世俗与上天的界限',
    ],
    'number9': [
        '数字9代表一个限度和界限',
        '数字9是力量和智慧的象征',
    ]
}


def main():
    with MoApp(appid='wx08fe2b1ff0c169f2', name='好友名字匹配', backgroundColor="#383838"):
        entrance()
        match()
        share()
        #share2()

def makeShareImage():
    ret = mo.acode.make('entrance', {})

    headimg = mo.token.get('host_headimg')
    canvas = mo.mopic.createCanvas(500, 500)
    canvas.addImage('http://img.mogodeer.cn/images/diudiu/name/erweima.jpg', pos=[0, 0, 500, 500])
    canvas.addImage(ret['url'], pos=[150, 250, 200, 200])
    #canvas.addImage(headimg, pos=[204, 305, 94, 94], mask='circle')
    mo.console( headimg)


    res = canvas.makeImage()
    if res['ret'] == 0:
        mo.token.set('share_image', res['url'])

# 创建结果相关的ui
def makeResultUI(name_header, x, y):
        with Box(pos=[x, y],size=[686, 1240]):
            Box(pos=[128, 74], size=[90, 90],border='0px solid #F56E6E',borderRadius='50%',background='#D03F3F')
            Image(name='%shost_avatar' %name_header,src='http://material.motimaster.com/appmaker/lijiong/2315.png', pos=[133, 79], size=[80, 80], borderRadius='50%',)
            Box(pos=[460, 74], size=[90, 90],border='0px solid #3E4DD2',borderRadius='50%',background='#3E4DD2')
            Image(name='%sguest_avatar' %name_header,src='img/head2.jpg', pos=[464, 79], size=[80, 80], borderRadius='50%')
            Box(pos=[269, 142], size=[140, 2],border='2px solid #F56E6E',borderRadius='0%',background='#F17093')
            Text(name='%sscore' %name_header, text='87分', pos=['center', 58],color='#F56E6E', fontSize=42)
            Text(name='%shost_name' %name_header, pos=[70, 170],size=[200,90],textAlign='center',color='#F56E6E', fontSize=24)
            Text(name='%sguest_name' %name_header, pos=[400, 170],size=[200,90],textAlign='center',color='#3E4DD2', fontSize=24)
            Image(src='img/jisuan1.jpg', pos=[25, 253], size=[630, 96],effect=fadein(size=(0,1),d=1,t=1,c=1,p=1,s=0))
            
            Text(name='%sw0' %name_header, pos=[43, 268],size=[63,63],textAlign='center',lineHeight=63,color='#F56E6E', fontSize=36,effect=bounceindown(size=(0,1),d=1,t=0.6,c=1,p=1,s=0))
            Text(name='%sw1' %name_header, pos=[152, 268],size=[63,63],textAlign='center',lineHeight=63,color='#3E4DD2', fontSize=36,effect=bounceindown(size=(0,1),d=1,t=0.6,c=1,p=1,s=0))
            Text(name='%sw2' %name_header, pos=[259, 268],size=[63,63],textAlign='center',lineHeight=63,color='#F56E6E', fontSize=36,effect=bounceindown(size=(0,1),d=1,t=0.6,c=1,p=1,s=0))
            Text(name='%sw3' %name_header, pos=[364, 268],size=[63,63],textAlign='center',lineHeight=63,color='#3E4DD2', fontSize=36,effect=bounceindown(size=(0,1),d=1,t=0.6,c=1,p=1,s=0))
            Text(name='%sw4' %name_header, pos=[472, 268],size=[63,63],textAlign='center',lineHeight=63,color='#F56E6E', fontSize=36,effect=bounceindown(size=(0,1),d=1,t=0.6,c=1,p=1,s=0))
            Text(name='%sw5' %name_header, pos=[579, 268],size=[63,63],textAlign='center',lineHeight=63,color='#3E4DD2', fontSize=36,effect=bounceindown(size=(0,1),d=1,t=0.6,c=1,p=1,s=0))
            
            Text(name='%snum00' %name_header, text='2', pos=[43, 334],size=[63,63],textAlign='center',lineHeight=63,color='#F56E6E', fontSize=30,effect=bounceindown(size=(0,1),d=1.5,t=0.6,c=1,p=1,s=0))
            Text(name='%snum01' %name_header, text='8', pos=[152, 334],size=[63,63],textAlign='center',lineHeight=63,color='#3E4DD2', fontSize=30,effect=bounceindown(size=(0,1),d=1.5,t=0.6,c=1,p=1,s=0))
            Text(name='%snum02' %name_header, text='4', pos=[259, 334],size=[63,63],textAlign='center',lineHeight=63,color='#F56E6E', fontSize=30,effect=bounceindown(size=(0,1),d=1.5,t=0.6,c=1,p=1,s=0))
            Text(name='%snum03' %name_header, text='6', pos=[364, 334],size=[63,63],textAlign='center',lineHeight=63,color='#3E4DD2', fontSize=30,effect=bounceindown(size=(0,1),d=1.5,t=0.6,c=1,p=1,s=0))
            Text(name='%snum04' %name_header, text='7', pos=[472, 334],size=[63,63],textAlign='center',lineHeight=63,color='#F56E6E', fontSize=30,effect=bounceindown(size=(0,1),d=1.5,t=0.6,c=1,p=1,s=0))
            Text(name='%snum05' %name_header, text='0',pos=[579, 334],size=[63,63],textAlign='center',lineHeight=63,color='#3E4DD2', fontSize=30,effect=bounceindown(size=(0,1),d=1.5,t=0.6,c=1,p=1,s=0))
            Image(src='img/jisuan2.jpg', pos=[72, 382], size=[544, 54],effect=fadein(size=(0,1),d=2,t=0.5,c=1,p=1,s=0))

            Text(name='%snum10' %name_header, text='4', pos=[101, 419],size=[63,63],textAlign='center',lineHeight=63,color='#333333', fontSize=30,effect=bounceindown(size=(0,1),d=2,t=0.6,c=1,p=1,s=0))
            Text(name='%snum11' %name_header, text='7', pos=[208, 419],size=[63,63],textAlign='center',lineHeight=63,color='#333333', fontSize=30,effect=bounceindown(size=(0,1),d=2,t=0.6,c=1,p=1,s=0))
            Text(name='%snum12' %name_header, text='8', pos=[313, 419],size=[63,63],textAlign='center',lineHeight=63,color='#333333', fontSize=30,effect=bounceindown(size=(0,1),d=2,t=0.6,c=1,p=1,s=0))
            Text(name='%snum13' %name_header, text='6', pos=[418, 419],size=[63,63],textAlign='center',lineHeight=63,color='#333333', fontSize=30,effect=bounceindown(size=(0,1),d=2,t=0.6,c=1,p=1,s=0))
            Text(name='%snum14' %name_header, text='0',pos=[518, 419],size=[63,63],textAlign='center',lineHeight=63,color='#333333', fontSize=30,effect=bounceindown(size=(0,1),d=2,t=0.6,c=1,p=1,s=0))
            Image(src='img/jisuan3.jpg', pos=[128, 467], size=[422, 57],effect=fadein(size=(0,1),d=2.5,t=0.5,c=1,p=1,s=0))
            
            Text(name='%snum20' %name_header, text='4', pos=[152, 505],size=[63,63],textAlign='center',lineHeight=63,color='#333333', fontSize=30,effect=bounceindown(size=(0,1),d=2.5,t=0.6,c=1,p=1,s=0))
            Text(name='%snum21' %name_header, text='7', pos=[261, 505],size=[63,63],textAlign='center',lineHeight=63,color='#333333', fontSize=30,effect=bounceindown(size=(0,1),d=2.5,t=0.6,c=1,p=1,s=0))
            Text(name='%snum22' %name_header, text='8', pos=[366, 505],size=[63,63],textAlign='center',lineHeight=63,color='#333333', fontSize=30,effect=bounceindown(size=(0,1),d=2.5,t=0.6,c=1,p=1,s=0))
            Text(name='%snum23' %name_header, text='6', pos=[472, 505],size=[63,63],textAlign='center',lineHeight=63,color='#333333', fontSize=30,effect=bounceindown(size=(0,1),d=2.5,t=0.6,c=1,p=1,s=0))
            Image(src='img/jisuan4.jpg', pos=[182, 554], size=[324, 56],effect=fadein(size=(0,1),d=3,t=0.5,c=1,p=1,s=0))
            
            Text(name='%snum30' %name_header, text='7', pos=[206, 593],size=[63,63],textAlign='center',lineHeight=63,color='#333333', fontSize=30,effect=bounceindown(size=(0,1),d=3,t=0.6,c=1,p=1,s=0))
            Text(name='%snum31' %name_header, text='8', pos=[313, 593],size=[63,63],textAlign='center',lineHeight=63,color='#333333', fontSize=30,effect=bounceindown(size=(0,1),d=3,t=0.6,c=1,p=1,s=0))
            Text(name='%snum32' %name_header, text='6', pos=[421, 593],size=[63,63],textAlign='center',lineHeight=63,color='#333333', fontSize=30,effect=bounceindown(size=(0,1),d=3,t=0.6,c=1,p=1,s=0))
            Image(src='img/jisuan5.jpg', pos=[237, 643], size=[215, 54],effect=fadein(size=(0,1),d=3.5,t=0.5,c=1,p=1,s=0))
            
            Text(name='%snum40' %name_header, text='8', pos=[262, 679],size=[63,63],textAlign='center',lineHeight=63,color='#333333', fontSize=30,effect=bounceindown(size=(0,1),d=3.5,t=0.6,c=1,p=1,s=0))
            Text(name='%snum41' %name_header, text='7', pos=[368, 679],size=[63,63],textAlign='center',lineHeight=63,color='#333333', fontSize=30,effect=bounceindown(size=(0,1),d=3.5,t=0.6,c=1,p=1,s=0))
            Image(src='img/jisuan6.jpg', pos=[292, 724], size=[108, 61],effect=fadein(size=(0,1),d=4,t=0.5,c=1,p=1,s=0))
            Text(name='%stotal_num' %name_header, text='87', pos=['center', 785],textAlign='center',lineHeight=63,color='#F56E6E', fontSize=45,effect=flipinx(size=(0,1),d=4,t=0.6,c=1,p=1,s=0))

# 名字叫home的页面
AUDITING = True
from moapp.lib.client import *
class entrance(Page):
    backgroundColor="#383838"
    background="#383838"
    barColor='#383838'
    barStyle='#383838'

    def UI(self):
        with Box(name='input_name_box', pos=[0,0], hidden=True, width=750):
            Image(name='image1',pos=[0,0],size=[750,1325],src="img/bg2.jpg")
            ImageAvatar(pos=['center', 30], size=[160,160], borderRadius='50%')
            Text(name='text1',text='你们的名字配不配？', color='#FFFFFF', fontSize=24, pos=['center', 400])
            Text(name='text2',text='汉字码加和取个位', color='#FFFFFF', fontSize=24, pos=['center', 450])
            Text(name='text3',text='算出你们的缘分', color='#FFFFFF', fontSize=24, pos=['center', 500])

            
            Input(name='input_host_name', pos= ['center',600], size=[480,80],
                  placeholder = '请输入你的名字', border='2px solid #F24040',background='255 255 255 0.3',color='#F46060',textAlign='center')
            Button(name='button1', text = '提交', pos=['center',938],size=[360,78],background = 'rgba(242,64,64,0.82)',
                                   lineHeight = 78,fontSize=36,fontWeight = 'bolder',borderRadius = '500px', 
                                   color = '#FFFFFF',boxShadow ='4px 8px 1px 3px rgba(0,0,0,0.2)',openType='getUserInfo',
                                   onTap = [moui.showLoading('加载中...'), self.commitName, moui.hideLoading()])
        with Box(name='auditing_box', pos=[0,0], hidden=True, width=750):
            Image(name='image1',pos=[0,-40],size=[750,1325],src="img/bg2.jpg")
            ImageAvatar(pos=['center', 30], size=[160,160], borderRadius='50%')
            Text(name='text1',text='算算好友跟你的名字能得多少分', color='#FFFFFF', fontSize=24, pos=['center', 400])
            Input(pos= ['center',500], size=[480,80],
                  placeholder = '请输入你的名字', border='2px solid #F24040',background='255 255 255 0.3',color='#F46060',textAlign='center')
            Input(pos= ['center',650], size=[480,80],
                  placeholder = '请输入对方的名字', border='2px solid #F24040',background='255 255 255 0.3',color='#F46060',textAlign='center')
            Button(name='button1', text = '提交', pos=['center',938],size=[360,78],background = 'rgba(242,64,64,0.82)',
                                   lineHeight = 78,fontSize=36,fontWeight = 'bolder',borderRadius = '500px', 
                                   color = '#FFFFFF',boxShadow ='4px 8px 1px 3px rgba(0,0,0,0.2)',openType='getUserInfo',
                                   onTap = [moui.showLoading('加载中...'), self.computeNameScore, moui.hideLoading()])

        with Box(name='loading_box', pos=[0,0], size=[750,1333]):
           
           Image(src='img/loading.png', size=[200, 200], pos=[275, 200],effect=rotate(deg=(0,360),d=0,t=2,c=0,p=0,s=0,o=(50,50)))
           Text(text='加载中,请稍后...', width=750, textAlign='center', color='#ffffff', pos=['center', 700])

    def computeNameScore():
        mo.showAlert('好友名字契合度','你们名字契合度分数为%s分'% str(int(random.random()*100)))
    
    def onInit():
        mo.console('main page init')
        page.loading_box.show()
        #inputNameBoxInit()
        if AUDITING == True:
            
            page.auditing_box.hidden = False
            page.loading_box.hidden = True
        else:
            inputNameBoxInit()
        

    def onPullDownRefresh():
        onInit()

    def inputNameBoxInit():
        mo.console('on inputNameBox init')
        page.input_host_name.value = user.nickName 
        mo.setNavibarTitle('好友姓名默契度')
        if mo.token.isHost(): #如果是主态
            tokenid = user.get('tokenid') #判断是否创建过令牌token
            if False:#tokenid != None: # 已经发起过匹配
                token = mo.getToken(tokenid)
                token.redirectTo('match') #带着令牌token跳转
            else:
                page.input_name_box.show() #没有匹配过 显示输入框
                page.loading_box.hide()
            
        else: #如果是客态
            if mo.token.getGuestInfo(user.openid) != None: #如果该用户已经匹配过用token redirectTo到match页面
                mo.token.redirectTo('match') 
            else:
                if user.get('name') != None:    # 已经全局输入过名字，直接使用自当匹配完
                    page.input_host_name.value = user.get('name')
                    #go_share2()
                    host_name = mo.token.get('host_name')
                    host = mo.token.getHostInfo()
                    mo.console('主人的信息 %s'% json.dumps(host))
                    mo.console('主人的名字%s' % host_name)
                    mo.console('客人的名字%s' % user.name )
                    #mo.console()

                    ret = calcName(host_name, host['gender'], user.get('name'), user.gender)
                    mo.console(ret)
                    mo.console(ret)
                    mo.token.markAsGuest({
                        'result': ret,
                        'name': user.get('name')
                    })
                    mo.token.redirectTo('match')
                    
                else:   # 没有输入过名字，显示输入框
                    page.loading_box.hide() 
                    page.input_name_box.show()
                    name = mo.token.get('host_name')
                    page.text2.text = '算一算 %s 跟你' %name
                    mo.setNavibarTitle('好友姓名默契度')
    #提交输入得姓名
    def commitName():
        name = page.input_host_name.value

        if not (2<= len(name) <=3):
            mo.showAlert('提示', '请输入2~3个汉字')
            return

        if not isAllChineseText(name):
            mo.showAlert('提示', '请输入2~3个汉字')
            return

        user.set('name', name)
        if mo.token.isHost():  #如果是主态
            mo.token.set('host_name', name)
            mo.token.set('host_headimg', user.avatarUrl)
            page.input_name_box.hide()
           
            user.set('tokenid', mo.token.id) #保存令牌tokem信息
            user.set('name', name)

            #page.sample_box.show()
            #显示示例box 初始化示例Box
            mo.token.redirectTo('match',mode='sample_mode')
        else: # 如果是客人态
            host_name = mo.token.get('host_name')
            host = mo.token.getHostInfo()
            ret = calcName(host_name, host['gender'], user.name, user.gender)
            mo.console(ret)
            mo.token.markAsGuest({
                'result': ret,
                'name': user.name
                })
            mo.token.redirectTo('match')
            #显示结果页
    
    
#匹配页面 一个例子Box 一个是匹配的box
class match(Page):
    backgroundColor="#383838"
    background="#383838"
    barColor='#383838'
    barStyle='#383838'  

    def UI(self):
        Image(name='banner1',hidden=True,src='http://material.motimaster.com/harvey///461a86c0052304000b0271c8e0b38388.jpeg',size=[750, 155])
        with Box(name='sample_box', pos=[0,0], hidden=True, width=750,background='#383838'):
            Image(name='page2image1',pos=[0,0],size=[750,339],src="img/bg3.jpg")
            #默契度计算list
            with Box(name='guest_list', pos=[33, 340], size=[686, 3050],border='1px solid #FFFFFF',borderRadius='0%',background='http://img.mogodeer.cn/images/diudiu/ceshi1/wnagge.jpg',boxShadow ='3px 3px 1px 3px rgba(208,63,63,0.9)'):
                Text(text='示例', pos=['center', 10],color='#F14141', fontSize=40)        
                Text(text='汉字码加和取个位，算出我们的缘分', pos=['center', 65],color='#333333', fontSize=22)
                makeResultUI('', 0, 50)                
                Box(pos=[0,940],background='rgba(0,0,0,0)',size=[200,200])

            Button(name='sharebutton1', text = '跟朋友圈好友算', position='fixed', left=380,bottom=30,size=[330,78],background = 'rgba(242,64,64,0.82)',border='1px solid #F24040',
                lineHeight = 78,fontSize=36,fontWeight = 'bolder',borderRadius = '5px', color = '#FFFFFF',boxShadow ='4px 8px 1px 3px rgba(0,0,0,0.2)',
                onTap=[moui.showLoading('请稍微等一下下...'), self.gotoSharePage, moui.hideLoading()])
            ShareButton(text='跟群好友算',position='fixed', left=50,bottom=30,size=[300,78], borderRadius = '5px',color='#FFFFFF',border='1px solid #F24040',
                fontSize=36,fontWeight = 'bolder',lineHeight=78,boxShadow ='4px 8px 1px 3px rgba(0,0,0,0.2)',background = 'rgba(242,64,64,0.82)',
                type='primary')
        with Box(name='match_box', hidden=False,pos=[0, 155], width=750, background='#383838'):
            Image(name='page2image1',pos=[0,0],size=[750,339],src="img/bg3.jpg")
            Text(name='tip1',text='暂时还没有好友来跟你匹配哦~',color='white',fontSize=40,pos=['center',420])
            Text(name='tip2',text='点击底部按钮邀请给好友开始计算',color='white',fontSize=40,pos=['center',520])
            with Box(name='guest_list', hidden=True, pos=[33, 335], size=[686, 1140],border='1px solid #FFFFFF',borderRadius='0%',background='http://img.mogodeer.cn/images/diudiu/ceshi1/wnagge.jpg',boxShadow ='3px 3px 1px 3px rgba(208,63,63,0.9)',marginBottom=50):
                makeResultUI('', 0, -20)                
                Text(name='wenan', background='white', text='', fontSize=27,pos=['center', 830], size=[600,300])
            with Box(pos=[0, 1530]):
                with List(name='rest_guests', position='relative', border='0px solid #FFFFFF',borderRadius='0%'):        
                    with Box(pos=[33, 0], size=[686, 150],border='0px solid #FFFFFF',borderRadius='0%',background='#D96363',boxShadow ='2px 2px 1px 2px rgba(255,255,255,1)',marginBottom=50):                        
                        Image(src='{item.host_avatar}', pos=[41, 15], size=[80, 80], border='4px solid #FFFFFF',borderRadius='50%')                
                        Image(src='{item.guest_avatar}', pos=[205, 15], size=[80, 80], border='4px solid #FFFFFF',borderRadius='50%')
                        Box(pos=[138, 58], size=[68, 2],border='2px solid #FFFFFF',borderRadius='0%',background='#FFFFFF')
                        Text(text='{item.score}分', pos=[373, 35],color='#FFFFFF', fontSize=42)
                        Text(text='{item.host_name}', pos=[36, 110],size=[90,24],textAlign='center',color='#FFFFFF', fontSize=20)
                        Text(text='{item.guest_name}', pos=[198, 110],size=[90,24],textAlign='center',color='#FFFFFF', fontSize=20)
                        Button(hidden='{item.hidden_show_detail}',text = '查看详情', lineHeight=45,fontSize=27,pos=[558, 50],size=[122,45],background = '#FFFFFF',
                               onTap=moui.request(self.showDetail, guest_openid='{item.guest_openid}'))
                        Button(hidden='{item.hidden_show_detail_guest}',text = '查看详情', lineHeight=45,fontSize=27,pos=[558, 50],size=[122,45],background = '#FFFFFF',
                               onTap=moui.showAlert('温馨提示:','只有主人能看哦~'))
                        Button(hidden='{item.hidden_show_detail_host}',text = '查看详情', lineHeight=45,fontSize=27,pos=[558, 50],size=[122,45],background = '#FFFFFF',
                               onTap=moui.confirm('温馨提示:',"查看全部好友的匹配详情（包括未来进入的好友），只需支付金额4.99元。",moui.request(self.onPay,guest_openid='{item.guest_openid}')))


                #Image(name='banner2',hidden=True,position='relative',src='http://material.motimaster.com/harvey///461a86c0052304000b0271c8e0b38388.jpeg',size=[750, 125])
                Image(name='banner2',hidden=True,pos=[33,0],src='http://material.motimaster.com/harvey///461a86c0052304000b0271c8e0b38388.jpeg',size=[686, 160])
                with Box(name='mad',width=686, position='relative',hidden=False,height='92px',pos=[33,0]):
                    AD(unitId='adunit-7f57f6c8c6c20904')
            
                Box(position='relative',size=[120,200],background='rgba(0,0,0,0)')
                
            Button(name='createbutton', text = '创建我的', position='fixed', left=195,bottom=30,size=[360,78],background = 'rgba(242,64,64,0.82)',
                lineHeight = 78,fontSize=36,fontWeight = 'bolder',borderRadius = '500px', color = '#FFFFFF',boxShadow ='4px 8px 1px 3px rgba(0,0,0,0.2)',openType='getUserInfo', 
                onTap=[moui.showLoading('请耐心等待一下...'),self.onCreateTap, moui.hideLoading()])
        # with Box(width=686, height='92px',pos=[33,0]):
        #     AD(unitId='adunit-7f57f6c8c6c20904')

            with Mask(name='match_detail_mask', hidden=True):
                with Box(pos=[33, 50], size=[686, 1200],border='1px solid #FFFFFF',borderRadius='0%',background='http://img.mogodeer.cn/images/diudiu/ceshi1/wnagge.jpg',boxShadow ='3px 3px 1px 3px rgba(208,63,63,0.9)',marginBottom=50):
                    makeResultUI('detail_', 0, 60)
                    Text(name='wenan2', background='white',text='', fontSize=28,pos=['center', 830], size=[600,300])


        with Box(name='loading_box', pos=[0,0], size=[750,1333],background='#383838'):           
           Image(src='img/loading.png', size=[200, 200], pos=[275, 200],effect=rotate(deg=(0,360),d=0,t=2,c=0,p=0,s=0,o=(50,50)))
           Text(text='加载中,请稍后...', width=750, textAlign='center', color='#ffffff', pos=['center', 700])

    #页面初始化
    def onInit():
        #mo.wxpay.pay('查看详情', 0.1, onPaySuccess, onPayFail)
        #page.mad.hidden = True
        page.banner2.hidden = True
        page.banner1.hidden = True
        mode = page.options.mode
        page.match_box.top = 0

        if mode != None and mode =='sample_mode':  #如果是主人刚进来 会是例子展示的box显示
            page.loading_box.hidden = True
            page.sample_box.hidden = False
            page.match_box.hidden = True
            match.sampleBoxInit()

        else: # 如果没有指定mode那就是显示匹配详情页面
             page.loading_box.hidden = True
             page.match_box.hidden = False
             match.matchBoxInit()

    def onPullDownRefresh():
        match.onInit()

    def onPay():
        page.data.guest_openid = params.guest_openid
        mo.wxpay.pay('查看详情', 4.99, onPaySuccess, onPayFail)
    
    def onPaySuccess(user, app, page, mo ):
        mo.console('支付成功')
        user.unlockall = True
        matchBoxInit()
        showDetail()

    def onPayFail(user, app, page, mo ):
        mo.console('支付失败')
    def matchBoxInit():
        if mo.token.isHost(): #主人态
            page.createbutton.text = '发送给好友开始计算'
            mo.setNavibarTitle('好友姓名默契度')
        else: #客人态
            page.createbutton.text = '创建我的'
            mo.setNavibarTitle('好友姓名默契度')

        guests = mo.token.getGuestList()
        mo.console(guests)
        host = mo.token.getHostInfo()
        mo.console(host)

        if len(guests)>0:
            page.tip1.hidden = True
            page.tip2.hidden = True
            last_guest_openid = None    # "最近的"访客openid
            if mo.token.isHost():       # 主人态，"最近的"就是最后一个
                last_guest_openid = guests[len(guests)-1]['openid']
            else:   # 客人态， "最近的"是"当前用户"
                last_guest_openid = user.openid

            host_name = mo.token.get('host_name')
            last_guest = mo.token.getGuestInfo(last_guest_openid)
            # last_guest['result'] = calcName(host_name, host['gender'], last_guest['name'], last_guest['gender'])
            page.host_avatar.src = host['avatarUrl']
            page.host_name.text = mo.token.get('host_name')            

            page.guest_avatar.src = last_guest['avatarUrl']
            page.guest_name.text = last_guest['name']

            page.score.text = '%d分' %last_guest['result']['score']

            page.w0.text = last_guest['result']['words'][0]
            page.w1.text = last_guest['result']['words'][1]
            page.w2.text = last_guest['result']['words'][2]
            page.w3.text = last_guest['result']['words'][3]            
            page.w4.text = last_guest['result']['words'][4]
            page.w5.text = last_guest['result']['words'][5]

            wenan = '详解：'
            wenan += DESCRIBE[int(last_guest['result']['score'])%len(DESCRIBE)]
            page.wenan.text = wenan

            process = last_guest['result']['process']
            page.num00.text = process[0][0]
            page.num01.text = process[0][1]
            page.num02.text = process[0][2]
            page.num03.text = process[0][3]
            page.num04.text = process[0][4]
            page.num05.text = process[0][5]

            page.num10.text = process[1][0]
            page.num11.text = process[1][1]
            page.num12.text = process[1][2]
            page.num13.text = process[1][3]
            page.num14.text = process[1][4]

            page.num20.text = process[2][0]
            page.num21.text = process[2][1]
            page.num22.text = process[2][2]
            page.num23.text = process[2][3]

            page.num30.text = process[3][0]
            page.num31.text = process[3][1]
            page.num32.text = process[3][2]

            page.num40.text = process[4][0]
            page.num41.text = process[4][1]

            page.total_num.text = last_guest['result']['score']

            # 剩下的人
            page.rest_guests.data = []
            for i in range(len(guests)):
                guest = guests[len(guests)-1-i]
                #if guest['openid'] != last_guest_openid: #user.openid:
                hidden_show_detail = False
                hidden_show_detail_guest = True
                hidden_show_detail_host = True

                # if mo.token.isHost()==True and user.unlockall!= None and user.unlockall ==True:
                #     hidden_show_detail = False
                #     hidden_show_detail_guest = True
                #     hidden_show_detail_host = True
                # elif mo.token.isHost() == True:
                #     hidden_show_detail = True
                #     hidden_show_detail_guest = True
                #     hidden_show_detail_host = False
                # elif mo.token.isHost() == False:
                #     hidden_show_detail = True
                #     hidden_show_detail_guest = False
                #     hidden_show_detail_host = True

                hidden_show_detail = False
                hidden_show_detail_guest = True
                hidden_show_detail_host = True

                page.rest_guests.data.append({
                        'host_name': host_name,
                        'host_avatar': host['avatarUrl'],
                        'guest_name': guest['name'],
                        'guest_openid': guest['openid'],
                        'guest_avatar': guest['avatarUrl'],
                        'score': guest['result']['score'],
                        'hidden_show_detail': hidden_show_detail,
                        'hidden_show_detail_guest': hidden_show_detail_guest,
                        'hidden_show_detail_host': hidden_show_detail_host,
                    })

            page.guest_list.show()
        else:
            page.tip1.hidden = False
            page.tip2.hidden = False
    def sampleBoxInit():
        mo.console('on sampleBoxInit')
        mo.setNavibarTitle('好友姓名默契度')
        mo.console(mo.token.get('host_name'))

        host = mo.token.getHostInfo()
        mo.console(host)

        host_name = mo.token.get('host_name')       
        last_guest = {
            'name': '特朗普',
            'avatarUrl': 'http://img.mogodeer.cn/images/diudiu/name/telangpu.jpg',
            'gender': 1
        }

        last_guest['result'] = calcName(host_name, host['gender'], last_guest['name'], last_guest['gender'])
        mo.console(last_guest['result'])
        page.host_avatar.src = host['avatarUrl']
        page.host_name.text = mo.token.get('host_name')            

        page.guest_avatar.src = last_guest['avatarUrl']
        page.guest_name.text = last_guest['name']

        page.score.text = '%d分' %last_guest['result']['score']

        page.w0.text = last_guest['result']['words'][0]
        page.w1.text = last_guest['result']['words'][1]
        page.w2.text = last_guest['result']['words'][2]
        page.w3.text = last_guest['result']['words'][3]
        page.w4.text = last_guest['result']['words'][4]
        page.w5.text = last_guest['result']['words'][5]

        process = last_guest['result']['process']
        page.num00.text = process[0][0]
        page.num01.text = process[0][1]
        page.num02.text = process[0][2]
        page.num03.text = process[0][3]
        page.num04.text = process[0][4]
        page.num05.text = process[0][5]

        page.num10.text = process[1][0]
        page.num11.text = process[1][1]
        page.num12.text = process[1][2]
        page.num13.text = process[1][3]
        page.num14.text = process[1][4]

        page.num20.text = process[2][0]
        page.num21.text = process[2][1]
        page.num22.text = process[2][2]
        page.num23.text = process[2][3]

        page.num30.text = process[3][0]
        page.num31.text = process[3][1]
        page.num32.text = process[3][2]

        page.num40.text = process[4][0]
        page.num41.text = process[4][1]

        page.total_num.text = last_guest['result']['score']
        page.guest_list.show()
        page.loading_box.hide()

    def onCreateTap(): 
        if mo.token.isHost(): #主人态去分享
            makeShareImage()
            mo.console('主人态，跳转到share Page')
            mo.token.goto('share')
        else: #客人态重定向为主人
            mo.console('客人态，重定向变为主态')
            #mo.redirectTo('create2'
            mo.redirectTo('entrance')

    def showDetail(): #显示匹配细节
        guest_openid = params.guest_openid
        if page.data.guest_openid != None:
            guest_openid = page.data.guest_openid
        host_name = mo.token.get('host_name')
        host = mo.token.getHostInfo()
        
        guest = mo.token.getGuestInfo(guest_openid)
        
        page.detail_host_avatar.src = host['avatarUrl']
        page.detail_host_name.text = mo.token.get('host_name')            

        page.detail_guest_avatar.src = guest['avatarUrl']
        page.detail_guest_name.text = guest['name']

        page.detail_score.text = '%d分' %guest['result']['score']

        page.detail_w0.text = guest['result']['words'][0]
        page.detail_w1.text = guest['result']['words'][1]
        page.detail_w2.text = guest['result']['words'][2]
        page.detail_w3.text = guest['result']['words'][3]                
        page.detail_w4.text = guest['result']['words'][4]
        page.detail_w5.text = guest['result']['words'][5]

        process = guest['result']['process']
        page.detail_num00.text = process[0][0]
        page.detail_num01.text = process[0][1]
        page.detail_num02.text = process[0][2]
        page.detail_num03.text = process[0][3]
        page.detail_num04.text = process[0][4]
        page.detail_num05.text = process[0][5]

        page.detail_num10.text = process[1][0]
        page.detail_num11.text = process[1][1]
        page.detail_num12.text = process[1][2]
        page.detail_num13.text = process[1][3]
        page.detail_num14.text = process[1][4]

        page.detail_num20.text = process[2][0]
        page.detail_num21.text = process[2][1]
        page.detail_num22.text = process[2][2]
        page.detail_num23.text = process[2][3]

        page.detail_num30.text = process[3][0]
        page.detail_num31.text = process[3][1]
        page.detail_num32.text = process[3][2]

        page.detail_num40.text = process[4][0]
        page.detail_num41.text = process[4][1]
        wenan2 = '详解：'
        # result_number = guest['result']['score']
        # num_set = set()
        # for num in str(result_number):
        #     num_set.add(num)
        # num_set.remove('0')
        # for num in num_set:
        #     if num !=0:
        #         wenan += random.choice(NUMBERS['number'+num]) + '\n'
        #wenan2 += random.choice(DESCRIBE)
        #wenan2 += DESCRIBE[0]
        wenan2 += DESCRIBE[int(guest['result']['score'])%len(DESCRIBE)]
        page.wenan2.text = wenan2

        page.detail_total_num.text = guest['result']['score']

        page.match_detail_mask.show()

    def onShare():
        page.share.page = 'entrance'

    def gotoSharePage():
        makeShareImage()
        #mo.token.goto('share')
        tokenid = user.get('tokenid')
        token = mo.getToken(tokenid)
        token.goto('share')

class share(Page):
    disableScroll = True
    title='姓名默契度'

    def UI(self):
       #Image(name='shareImage',src='http://material.motimaster.com/yuyuan/Duudle/create/ec26c4802daf55428cbe6a79ec72f176.png',pos=[15,10,720,722])
       Image(name='shareImage',src='http://img.mogodeer.cn/images/diudiu/xingzuozhun/erweima5.jpg', pos=['center',23], size=[700,700])
       #ImageAvatar(name='avatar',pos=[297,393,149,149],borderRadius='50%')
       Button(name='saveShareImage',onTap=[moui.showLoading(),self.saveShareImage,moui.hideLoading()],text='保存朋友圈海报',fontWeight=900,lineHeight=80,pos=[175,780,400,80], boxShadow='-1px 10px 5px -5px #BBBBBB',fontSize='16px', color='#ffffff',border='1px solid #ffffff',backgroundColor="rgba(242,64,64,0.82)")
       ShareButton(text='分享到好友群',pos=[175,923,400,80], color='#F24040',border='1px solid #F24040',fontSize='16px',lineHeight=80,boxShadow='-1px 3px 5px -5px #BBBBBB',backgroundColor="#ffffff",type='primary')

    def onInit():
        page.shareImage.src = mo.token.get('share_image')

    def saveShareImage():
        mo.saveImage(mo.token.get('share_image'))

    def onShare():
        page.share.page = 'entrance'





# if __name__ == '__main__':
#     try:
#         main()
#     except Exception as ex:
#         exc_type, exc_value, exc_tb = sys.exc_info()
#         print('错误信息: '+str(exc_value), file=sys.stderr)
#         last_tb = traceback.extract_tb(exc_tb).pop()
#         if last_tb:
#             if last_tb.filename.find("/mogo/codes/") == -1:
#                 print('出错文件: ' + last_tb.filename, file=sys.stderr)
#                 print('出错代码: ' + last_tb.line, file=sys.stderr)
#                 print('出错代码行: ' + str(last_tb.lineno), file=sys.stderr)
#             else:
#                 print('出错文件: 错误写法导致框架代码报错', file=sys.stderr)
#                 print('traceback:' + traceback.format_exc())

#         sys.exit(-1)
    
