   M S B A M L   `   `   `  ����F  BBookLibrary, Version=0.0.0.0, Culture=neutral, PublicKeyToken=nullq=clr-namespace:Waf.BookLibrary.Library.Presentation.Properties/Waf.BookLibrary.Library.Presentation.Properties  5      q=clr-namespace:Waf.BookLibrary.Library.Presentation.DesignData/Waf.BookLibrary.Library.Presentation.DesignData  5      ;    5Waf.BookLibrary.Library.Presentation.Views.PersonView   5      \ XPresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35R NWindowsBase, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35W SPresentationCore, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35D 9http://schemas.microsoft.com/winfx/2006/xaml/presentation    5      R NSystem.Xaml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089:x,http://schemas.microsoft.com/winfx/2006/xaml     5      Kp=clr-namespace:Waf.BookLibrary.Library.Presentation.Properties     5      @d2http://schemas.microsoft.com/expression/blend/2008     5      Jmc;http://schemas.openxmlformats.org/markup-compatibility/2006     5      K GSystem.Waf.Wpf, Version=5.0.0.100, Culture=neutral, PublicKeyToken=null)wafhttp://waf.codeplex.com/schemas  5      Fdd=clr-namespace:Waf.BookLibrary.Library.Presentation.DesignData  5      $	��250��5
      $	��122��6   .  (System.Waf.Presentation.ValidationHelper    	IsEnabled  . {�6$   �� *	IsEnabled+   IsValid 5   +   �� *	IsValid+ �� Mode$ OneWayToSource=�.��5      � $��11,11,22,11q�6    � ColumnDefinitions 5   
   �� 5      $
��Auto �6   �� 5         Layout.LargeColumnSpace#��[  6   �� 5      $��* �6   �� 5        Layout.ColumnSpace#��[ 6   �� 5      $
��Auto �6    � RowDefinitions 5   
   �� 5      $
��Auto �6   �� 5        Layout.RowSpace#��[ 6   �� 5      $
��Auto �6   �� 5      #��[ 6   �� 5      $
��Auto �6   �� 5      $��* �6   .+�5   
   �� $��0��6   $��0��6    ?   9Waf.BookLibrary.Library.Presentation.Properties.Resources   FirstnameMenu#��Z 6-    �� Target 6\   ��  �� ElementName$ firstnameBox���� 5   
   -   5         ��Name$ firstnameBox��5      $��2��6(   $��0��68   $��3��6E   	 �� 	MaxLength$	 30��5!      $��Stretch=�6!   ��5       �� *Person.Firstname+
 �� UpdateSourceTrigger$
 PropertyChanged=� �� ValidatesOnExceptions .  �� NotifyOnValidationError . 5!   !   �� 5#   
   $��0��6   $��2��6       Lastname#��Z 6-   �� 5$   
   $��2��6   $��2��6"   $��3��6/   $	 30��5%      $��Stretch=�6!   ��5$   C   �� *Person.Lastname+$
 PropertyChanged=� .  . 5%   !   �� 5'   
   $��0��6   $��4��6       Email#��Z 6-   �� 5(   
   $��2��6   $��4��6"   $		 100��5)      $��Stretch=�6"   ��5(   /   �� *Person.Email+$
 PropertyChanged=� .  . 5)   "   �� 5*   
   $��4��6   $��4��6!     
EmailImage#��[ 6�      NewEmailMessage � ToolTip# Z 5+      $��25��6B    � UseLayoutRounding . ��5*   .   �� *CreateNewEmailCommand+��6X   �� *Person+" �� ValidatesOnNotifyDataErrors .  5+   P   5,      5-      