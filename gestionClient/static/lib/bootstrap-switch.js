INDX( 	 E>	            (   ?  ?       ?9 e     S ?        ?@     ? ?     ?@     O?8????????'?z????????? ?r    ??r            1 1 .   I n t r o d u c t i o n   t o   t h e   p r o j e c t   (   6 9 4   X   1 2 8 0   ) . m p 4     ?@     ? ?     ?@     `ڄ)??? ???'??r+???#WM+??? ?$    ??$            = 1 0 .   C r e a t i n g   M a i n   M e n u   a n d   I n f i n i t e   L o a d e r   (   6 9 4   X   1 2 8 0   ) . m p 4    ?@     ? ?     ?@     f u+??? Մ??'?_??,??????,??   d    ?d            < 1 1 .   I m p l e m e n t i n g   S e a r c h   B a r   F u n c t i o n a l i t y   (   6 9 4   X   1 2 8 0   ) . m p 4      ?@     ? ?     ?@     S??,??? C???'?Y?.???)?.??? P    ~A            4 1 2 .   F i n i s h i n g   S i n g l e   P r o d u c t   P a g e   (   6 9 4   X   1 2 8 0   ) . m p 4      ?@     ? ?     ?@     ?z?.?????[X?'????0???|a?0??? p@    k@            9 1 3 .   I m p l e m e n t i n g   S o r t i n g   F u n c t i o n a l i t y   (   6  4   X   1 2 8 0   ) . m p 4     ?@     ? ?     ?@     ???0????L@??'?d/?4???nO`4??? P    C            8 1 4 .   I m p l e m e n t i n g   F i l t e r   F u n c t i o n a l i t y   (   6 9 4   X   1 2 8 0   ) . m p 4 ?     ?@     ? ?     ?@     3??4????݌Y?'?aF7???D?7??? ??    ??            , 1 5 .   C a r t   S e r v i c e   -   P a r t   1   (   6 9 4   X   1 2 8 0   ) . m p 4 0   ) ?@     ? ?     ?@     .?H7??? ???'?x?U:???{?:??? P?    ?O?            , 1 6 .   C a r t   S  r v i c e   -   P a r t   2   (   6 9 4   X   1 2 8 0   ) . m p 4 0   ) ?@     ? ?     ?@     4?X:??? 
?)?'?"?>?????>??? ??    ??            1 1 7 .   C h e c k o u t   a n d   T h a n k Y o u   P a g e   (   6 9 4   X   1 2 8 0   ) . m p 4 p 4 ?@     ? ?     ?@     ㆣ>??? ? ?'?Y??@????F?@??? p?    j?            6 1 8 .   C r e a t i n g   A u t h e n t i c a t i o n   S e r v i c e   (   6 9 4   X   1 2 8 0   ) . m p 4  ?@     ? ?     ?@     ???@??? ???'?QC???:)?B??? ?S   v?S            & 1 9 .   U s e r   L o g i n   P a g e   (   6 9 4   X   1 2 8 0   ) . m p 4   ?@     ? ?     ?@     ??#??? \???'?|h?????ް???  ?     ??             3 2 .   P r e - r e q u i s i t e s   o f   t h e   p r o j e c t   (   6 9 4   X   1 2 8 0   ) . m p 4 ?@      ?     ?@     ?Ǽ??????s?'?]h5????????? 0?    ?*?            U 3 .   C r e a t i n g   A   N e w   I o n i c - A n g u l a r   P r o j e c t   a n d   W o r d P r e s s   I n s t a l l a t i o n   (   6 9 4   X  1 2 8 0   ) . m p 4     ?@     ? ?     ?@     ??7??? ??R?'??!???(?? ???  ?    ???            . 4 .   C o n f i g u r i n g   S S L   i n   X A M P P   (   6 9 4   X   1 2 8 0   ) . m p 4   ?@     ? ?     ?@     ?m!??? ??S?'????"????{"??? ?n    ??n            5 5 .   E x p l o r i n g   O u r   N e w   I o n i c   P r o j e c t   (   6 9 4   X   1 2 8 0   ) . m p 4     ?@     ? ?     ?@     ??"??? ܁2?'?$+}$???jST$??? @     w=             G 6 .   A d d i n g   A n d r o i d    u p p o r t   &   C r e a t i n g   P r o d u c t   S e r v i c e   (   6 9 4   X   1 2 8 0   ) . m p 4 ?@     ? ?     ?@     ԅ?$??? ?=?'?&Ɋ%???Fx%??? @?    ?<?            2 7 .   D e s i g n i n g   S h o p   T a b   -   T o o l B a r   (   6 9 4   X   1 2 8 0   ) . m p 4   ?@     ? ?     ?@     &Ɋ%????6j??'?֖`(??? $$(??? ?    ??            2 8 .   D e s i g n i n g   S h o p   T a b   -   C o n t e n t   (   6 9 4   X   1 2 8 0   ) . m p 4   ?@     ? ?     ?@     ? c(????ߖ??' @?)?????k)??? ??    ??            C 9 .   C r e a t i n g   A n g u l a r   H T T P   I n t e r c e p t o r   F o r   B a c k e n d   (   6 9 4   X   1 2 8 0   ) . m p 4                                                                                                                                                                                                                                                                                                                                              f ($element.data('animated') !== false)
                  $element.addClass("switch-animate");

                $element.parent().trigger('switch-change', {'el': $this, 'value': thisState})
              }
            });

            $element.find('label').on('mousedown touchstart', function (e) {
              var $this = $(this);
              moving = false;

              e.preventDefault();
              e.stopImmediatePropagation();

              $this.closest('div').removeClass('switch-animate');

              if ($this.closest('.has-switch').is('.deactivate'))
                $this.unbind('click');
              else {
                $this.on('mousemove touchmove', function (e) {
                  var $element = $(this).closest('.switch')
                    , relativeX = (e.pageX || e.originalEvent.targetTouches[0].pageX) - $element.offset().left
                    , percent = (relativeX / $element.width()) * 100
                    , left = 25
                    , right = 75;

                  moving = true;

                  if (percent < left)
                    percent = left;
                  else if (percent > right)
                    percent = right;

                  $element.find('>div').css('left', (percent - right) + "%")
                });

                $this.on('click touchend', function (e) {
                  var $this = $(this)
                    , $target = $(e.target)
                    , $myCheckBox = $target.siblings('input');

                  e.stopImmediatePropagation();
                  e.preventDefault();

                  $this.unbind('mouseleave');

                  if (moving)
                    $myCheckBox.prop('checked', !(parseInt($this.parent().css('left')) < -25));
                  else $myCheckBox.prop("checked", !$myCheckBox.is(":checked"));

                  moving = false;
                  $myCheckBox.trigger('change');
                });

                $this.on('mouseleave', function (e) {
                  var $this = $(this)
                    , $myCheckBox = $this.siblings('input');

                  e.preventDefault();
                  e.stopImmediatePropagation();

                  $this.unbind('mouseleave');
                  $this.trigger('mouseup');

                  $myCheckBox.prop('checked', !(parseInt($this.parent().css('left')) < -25)).trigger('change');
                });

                $this.on('mouseup', function (e) {
                  e.stopImmediatePropagation();
                  e.preventDefault();

                  $(this).unbind('mousemove');
                });
              }
            });
          }
        );
      },
      toggleActivation: function () {
        $(this).toggleClass('deactivate');
      },
      isActive: function () {
        return !$(this).hasClass('deactivate');
      },
      setActive: function (active) {
        if (active)
          $(this).removeClass('deactivate');
        else $(this).addClass('deactivate');
      },
      toggleState: function (skipOnChange) {
        var $input = $(this).find('input:checkbox');
        $input.prop('checked', !$input.is(':checked')).trigger('change', skipOnChange);
      },
      setState: function (value, skipOnChange) {
        $(this).find('input:checkbox').prop('checked', value).trigger('change', skipOnChange);
      },
      status: function () {
        return $(this).find('input:checkbox').is(':checked');
      },
      destroy: function () {
        var $div = $(this).find('div')
          , $checkbox;

        $div.find(':not(input:checkbox)').remove();

        $checkbox = $div.children();
        $checkbox.unwrap().unwrap();

        $checkbox.unbind('change');

        return $checkbox;
      }
    };

    if (methods[method])
      return methods[method].apply(this, Array.prototype.slice.call(arguments, 1));
    else if (typeof method === 'object' || !method)
      return methods.init.apply(this, arguments);
    else
      $.error('Method ' + method + ' does not exist!');
  };
}(jQuery);

$(function () {
  $('.switch')['bootstrapSwitch']();
});
