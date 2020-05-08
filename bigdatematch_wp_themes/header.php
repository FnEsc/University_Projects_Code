<!DOCTYPE html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<style media="screen"></style>
<title>
  <?php if ( is_home() ) {
            bloginfo('name');
            } elseif ( is_category() ) {
            single_cat_title(); echo " - "; bloginfo('name');
            } elseif (is_single() || is_page() ) {
            single_post_title();
            } elseif (is_search() ) {
            echo "搜索结果"; echo " - "; bloginfo('name');
            } elseif (is_404() ) {
            echo '页面未找到!';
            } else {
            wp_title('',true);
            }
        ?>
</title>
<meta name="keywords" content="模版编号001lt263-贴心大学">
<meta charset="utf-8">
<meta name="description" content="我行我数大数据应用创新大赛，佛山科学技术学院我行我数大数据应用创新大赛">
<meta name="renderer" content="webkit">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<link rel="stylesheet" type="text/css" href="<?php bloginfo('template_directory'); ?>/css/main.css">
</head>
<body>
<!--头部-->
<script type="text/javascript" src="<?php bloginfo('template_directory'); ?>/js/jquery-1.7.2.min.js"></script>
<script type="text/javascript" src="<?php bloginfo('template_directory'); ?>/js/jquery.KinSlideshow-1.2.1.min.js"></script>
<script type="text/javascript" src="<?php bloginfo('template_directory'); ?>/js/MSClass.js"></script>
<script type="text/javascript" src="<?php bloginfo('template_directory'); ?>/js/DD_belatedPNG_0.0.8a.js"></script>
<script type="text/javascript" src="<?php bloginfo('template_directory'); ?>/js/jquery.pagination.js"></script>
<script type="text/javascript" src="<?php bloginfo('template_directory'); ?>/js/base.js"></script>
<script type="text/javascript" src="<?php bloginfo('template_directory'); ?>/js/tabList.js"></script>
<script type="text/javascript" src="<?php bloginfo('template_directory'); ?>/js/comm.js"></script>

<!--头部-->
<div class="header">
    <div class="hd-zz">
        <div class="header-content">
        	<div class="logo">
        		<a href="http://www.fosu.edu.cn/"><img src="<?php bloginfo('template_directory'); ?>/images/logo.png" style="width: 400px;height: 95px;float: left;"></a>
        	</div>
            <div class="tittle_2"><a href="<?php echo get_option('home'); ?>" class="a1">我行我数<b>__</b>大数据应用创新大赛</a></div>
          <div class="clear"></div>
            <!--搜索-->

        </div>
    </div>
    <div class="menu">
       <ul id="nav">
           <?php
            wp_nav_menu( array( 'theme_location'=>'PrimaryMenu', 'container_class' => 'on', 'depth' => 2) );
    ?>

        </ul>
    </div>
</div>
<div class="clear"></div>
<!--头部-->