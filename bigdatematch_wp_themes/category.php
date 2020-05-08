<?php get_header();?>
<!--头部-->
<div class="container ny-container">
    <div class="content ny-content">
    <?php get_sidebar ();?>
  <div class="ny-right">
    <div class="ny-right-title"> 当前位置：<?php wheatv_breadcrumbs(); ?> </div>
    <div class="ny-right-content news-list02">
      <ul>
                    <!-- 文章顶置 -->
                    <!-- <?php   query_posts(array("category__in" => array(get_query_var("cat")), "post__in" => get_option("sticky_posts")));
                            while(have_posts()) : the_post(); ?>
                    <li>
                        <a href="">【顶置】<?php the_title(); ?></a><span><?php the_time('Y-m-d') ?></span>
                    </li>
                    <?php endwhile;wp_reset_query(); ?> -->
                    <!-- end文章顶置 -->
        <?php wp_reset_query(); ?>
        <?php while (have_posts()) : the_post(); ?><?php if(!is_sticky()){ ?>
            <li>
               <a href="<?php the_permalink(); ?>"><?php the_title(); ?></a><span><?php the_time('Y-m-d') ?></span>
            </li>
        <?php } endwhile; ?>

      </ul>
      <div class="clear"> </div>
      <div class="paging right">
        <div class="manu">
          <?php par_pagenavi(9); ?>
        </div>
      </div>
    </div>
    <div class="ny-right-bottom"></div>
  </div>
  </div>
</div>
<!--尾部-->
<!--底部-->
<?php get_footer();?>