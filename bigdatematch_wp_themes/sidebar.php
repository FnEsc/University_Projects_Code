      <div class="ny-left">
        <div class="ny-left-title">
          <?php
               //如果是列表页则这样
                if(is_category()){
                  $cat_id = $cat;
                  $catetory = get_category($cat_id);
                  // echo "<li>";
                  echo $catetory->cat_name;
                  // echo '</li>';
                }
                //如果是内容页则这样
                if(is_single()){
                  $category = get_the_category();
                  $cat_id = $category[0]->cat_ID;
                  //var_dump($category);
                  // echo "<li>";
                    echo $category[0]->cat_name;
                    // echo '</li>';
                }
              ?>
        </div>
        <div class="ny-left-content">
          <ul style="display: block;">
            <!-- <?php if(is_single()||is_category()){
              if(get_category_children(get_category_root_id(the_category_id(false)))!= "" ){
                                                echo wp_list_categories("child_of=".get_category_root_id(the_category_id(false)). "&depth=0&hide_empty=0&title_li=&orderby=id&order=asc");
                                            }
                                            else echo"基于当代大学生个人电脑桌面使用的调查报告正文";
                                        }
                                    ?> -->
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;报告正文
          </ul>
        </div>
        <div class="ny-left-bottom"></div>
      </div>