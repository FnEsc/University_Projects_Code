<?php get_header();?>
<!--头部-->
<!--头部-->
<!--主体-->
<div class="container">
<div class="content index-content">
<!--上部分-->
    <div class="con-top">
        <div class="bg">
	<div class="slide">
          <?php
    echo do_shortcode("[metaslider id=154]");
?>
    </div>
            <!--S area1-->
            <div class="area1">
                <div class="title">
                    <?php query_posts(array('category_name'=>'','orderby'=>date,'order'=>ASC,'posts_per_page'=>1)); ?>
                    <div class="tl"><!-- <?php single_cat_title(); ?> -->作品概况</div>
                    <div class="more"><a href="">更多 &nbsp;&gt;&gt;</a></div>
                    <?php wp_reset_query() ?>
                </div>
                <div class="area-con">
                    <div class="area1-con-top">
                    <?php query_posts(array('category_name'=>'zpjj','orderby'=>date,'order'=>ASC,'posts_per_page'=>1)); ?>
                    <?php if ( have_posts() ) : while ( have_posts() ) : the_post(); ?>
                        <?php thumb_img($post->post_content);?>
                        <p><?php echo mb_strimwidth(strip_tags(apply_filters('the_content', $post->post_content)), 0, 350,"..."); ?><a href="<?php the_permalink(); ?>">【详细】</a></p>
                        <?php endwhile; ?>
                        <?php else: ?><h3>找不到文章</h3><?php endif; ?>
                        <?php wp_reset_query() ?>
                    </div>
                    <!-- <ul>
                      <?php query_posts(array('category_name'=>'','orderby'=>date,'order'=>ASC,'posts_per_page'=>4)); ?>
                      <?php if ( have_posts() ) : while ( have_posts() ) : the_post(); ?>
                      <li>
                        <a href="<?php the_permalink(); ?>" title="<?php the_title();?>" target="#target"><?php echo wp_trim_words( get_the_title(), 20 );?></a><span><?php echo the_time('Y-m-d');?></span>
                      </li>
                      <?php endwhile; ?>
                      <?php else: ?><h3>找不到文章</h3><?php endif; ?>
                      <?php wp_reset_query() ?>
                    </ul> -->
                </div>
            </div>
            <!--E area1-->
            <!--S area2-->
            <div class="area2">
                <div class="title">
                   <?php query_posts(array('category_name'=>'sjfxyjl','orderby'=>date,'order'=>ASC,'posts_per_page'=>1)); ?>
                    <div class="tl"><!-- <?php single_cat_title(); ?> -->数据分析</div>
                    <div class="more"><a href="">更多 &nbsp;&gt;&gt;</a></div>
                </div>
                <div class="area-con">
                    <!-- 图片 -->
                    <?php if ( have_posts() ) : while ( have_posts() ) : the_post(); ?>
                    <?php thumb_img($post->post_content);?>
                    <p><!-- 350字文章 --><?php echo mb_strimwidth(strip_tags(apply_filters('the_content', $post->post_content)), 0, 350,"..."); ?><a href="<?php the_permalink(); ?>">【详细】</a></p>
                     <?php endwhile; ?>
                      <?php else: ?><h3>找不到文章</h3><?php endif; ?>
                      <?php wp_reset_query() ?>
                </div>
            </div>
            <!--E area2-->
        </div>
    </div>
    <!--上部分-->
  <div class="con-bot">
        <div class="bg">
            <div class="link1">
                <ul>
                    <li class="li1"><a href="http://web.fosu.edu.cn/" target="target=" _self""="">佛山科学技术学院</a></li>
                    <li class="li2"><a href="http://newscenter.southcn.com/n/node_342572.htm" target="target=" _blank""="">大赛最新动态</a></li>
                    <li class="li3"><a href="https://sojump.com/jq/13746251.aspx" target="target=" _self""="">问卷调查表</a></li>
                    <li class="li4"><a href="http://newscenter.southcn.com/n/2016-05/27/content_148434499.htm" target="target=" _self""="">决赛候选名单</a></li>
                </ul>
            </div>
            <div class="link2">
                <div class="link2-tl">友情链接</div>
                <div class="link2-con">
                    <ul>
                        <li><a href="http://web.fosu.edu.cn/eie/" target="target=" _self""="">佛大电信学院</a></li>
                        <li><a href="http://www.china.com.cn/" target="target=" _blank""="">中国网</a></li>
                        <li><a href="http://www.xinhuanet.com/" target="target=" _blank""="">新华网</a></li>
                        <li><a href="http://www.southcn.com/" target="target=" _blank""="">南方网</a></li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
    <!--下部分-->
</div>
</div>
<!--主体-->
<!--底部-->

<!--底部-->
<?php get_footer();?>