   M S B A M L   `   `   `  ����F  BBookLibrary, Version=0.0.0.0, Culture=neutral, PublicKeyToken=nullq=clr-namespace:Waf.BookLibrary.Library.Presentation.Properties/Waf.BookLibrary.Library.Presentation.Properties  5      q=clr-namespace:Waf.BookLibrary.Library.Presentation.DesignData/Waf.BookLibrary.Library.Presentation.DesignData  5      9    3Waf.BookLibrary.Library.Presentation.Views.BookView   5      \ XPresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35R NWindowsBase, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35W SPresentationCore, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35D 9http://schemas.microsoft.com/winfx/2006/xaml/presentation    5      R NSystem.Xaml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089:x,http://schemas.microsoft.com/winfx/2006/xaml     5      Kp=clr-namespace:Waf.BookLibrary.Library.Presentation.Properties     5      @d2http://schemas.microsoft.com/expression/blend/2008     5      Jmc;http://schemas.openxmlformats.org/markup-compatibility/2006     5      K GSystem.Waf.Wpf, Version=5.0.0.100, Culture=neutral, PublicKeyToken=null)wafhttp://waf.codeplex.com/schemas  5      Fdd=clr-namespace:Waf.BookLibrary.Library.Presentation.DesignData  5      $	��250��5
      $	��270��6   .  (System.Waf.Presentation.ValidationHelper    	IsEnabled  . {�6$   �� *	IsEnabled+   IsValid 5   +   �� *	IsValid+ �� Mode$ OneWayToSource=�.��5      � $��11,11,22,11q�6    � ColumnDefinitions 5   
   �� 5      $
��Auto �6   �� 5         Layout.LargeColumnSpace#��[  6   �� 5      $��* �6   �� 5        Layout.ColumnSpace#��[ 6   �� 5      $
��Auto �6    � RowDefinitions 5   
   �� 5      $
��Auto �6   �� 5        Layout.RowSpace#��[ 6   �� 5      $
��Auto �6   �� 5      #��[ 6   �� 5      $
��Auto �6   �� 5      #��[ 6   �� 5      $
��Auto �6   �� 5      #��[ 6   �� 5      $
��Auto �6   �� 5      #��[ 6   �� 5       $
��Auto �6   �� 5!      #��[ 6   �� 5"      $
��Auto �6   �� 5#      #��[ 6   �� 5$      $
��Auto �6   �� 5%      $��* �6   .+�5(   
   �� $��0��6   $��0��6    ?   9Waf.BookLibrary.Library.Presentation.Properties.Resources   	TitleMenu#��Z 6-    �� Target 6X   ��  �� ElementName$ titleBox���� 5)   
   -   5         ��Name$ titleBox��5)      $��2��6$   $��0��64   $��3��6A   	 �� 	MaxLength$		 100��5+      $��Stretch=�6"   ��5*      �� *
Book.Title+
 �� UpdateSourceTrigger$
 PropertyChanged=� �� ValidatesOnExceptions .  �� NotifyOnValidationError . 5+   "   �� 5-   
   $��0��6   $��2��6       Author#��Z 6-   �� 5.   
   $��2��6   $��2��6"   $��3��6/   $		 100��50      $��Stretch=�6"   ��5/      �� *Book.Author+$
 PropertyChanged=� .  . 50   "   �� 52   
   $��0��6   $��4��6       	Publisher#��Z 6-   �� 53   
   $��2��6   $��4��6"   $��3��6/   $		 100��55      $��Stretch=�6"   ��54      �� *Book.Publisher+$
 PropertyChanged=� .  . 55   "   �� 57   
   $��0��6   $��6��6       PublishDate#��Z 6-   (  "System.Windows.Controls.DatePicker  58   
   $��2��6   $��6��6%   $��3��62   $��Stretch=�59         SelectedDate 58   F   �� *Book.PublishDate+59      �� 5;   
   $��0��6   $��8��6       Isbn#��Z 6-   �� 5<   
   $��2��6   $��8��6"   $��3��6/   $	 14��5>      $��Stretch=�6!   ��5=      �� *	Book.Isbn+$
 PropertyChanged=� .  . 5>   !   �� 5@   
   $��0��6   $��10��6       Language#��Z 6.   �� 5A   
   $��2��6   $��10��6#   $��3��61   $��24��5B   :   ��5A   E   ��   LanguageValues �� Source# [  �� SelectedItem 5B      �� *Book.Language+��5C      �� 5D      .R�5E      �� ��6    ��   LanguageToStringConverter �� 	Converter# [ 5F      5H      �� 5J   
   $��0��6   $��12��6       Pages#��Z 6.   �� 5K   
   $��2��6   $��12��6"   $��3��60   $��Stretch=�5M      ��5L      �� *
Book.Pages+$
 PropertyChanged=� .  . 5M      �� 5O   
   $��0��6   $��14��6       LendTo#��Z 6.   �� 5P   
   $��2��6   $��14��6"    �� 
IsReadOnly . $��Stretch=�6B   .��6`   ��5Q      `� 5R       �� StringFormat$ {0} {1}��6   " `� ValidatesOnNotifyDataErrors .  .1�5S      ��  �� Path$ Book.LendTo.Firstname�6   �� 5T      $ Book.LendTo.Lastname�6   5U      .��5V      5W      �� 5X   
   $��4��6   $��14��6!      
MoreButton#��Z 5Y   t   $��25��5Z      ��5Y      �� *LendToCommand+��6/   �� *Book+" �� ValidatesOnNotifyDataErrors .  5Z      5[      5]      