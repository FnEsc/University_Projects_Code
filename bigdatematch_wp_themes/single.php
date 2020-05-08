<?php get_header();?>
<!--头部-->
<!--头部-->
<div class="container ny-container">
<div class="content ny-content">
  <?php get_sidebar ();?>
  <div class="ny-right">
    <div class="ny-right-title"> 当前位置：<?php wheatv_breadcrumbs(); ?></div>
    <div class="ny-right-content">
      <h1 class="right-main-title"><?php the_title_attribute(); ?></h1>
      <div class="right-sub-title"><span><?php the_time('Y/m/d') ?><!-- </span>13人浏览</span> --></div>
        <?php if (have_posts()) : ?>
        <?php while (have_posts()) : the_post(); ?>
      <div class="right-main-show">
       <?php the_content(); ?></div>
     <?php endwhile?>
     <?php else : ?>
     <?php endif ?>
      <div class="clear"> </div>
      <div class="next-page">
        <ul>
            <li><?php if (get_previous_post()) { previous_post_link('上一篇: %link');} else {echo "已是最后文章";} ?></li>
            <li><?php if (get_next_post()) { next_post_link('下一篇: %link');} else {echo "已是最新文章";} ?></li>
        </ul>
      </div>
      <!--评论部分-->

      <!--评论部分-->
    </div>
    <div class="ny-right-bottom"></div>
  </div>
</div>
</div>
<!--尾部-->
<!--底部-->
<?php get_footer();?>