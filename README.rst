Android-MissingDrawables
========================

Check if your Drawables are present in all density buckets. Example::

    $ sudo pip install android-missingdrawables
    $ missingdrawables ~/projects/AwesomeApp/res
                                             l  |  m  |  h  |  xh 
                             action_g.png |  +  |  +  |  +  |  +  |
                           action_pin.png |  +  |  +  |  -  |  +  |
                        action_search.png |  +  |  -  |  +  |  +  |
                      action_wishlist.png |  +  |  +  |  +  |  +  |
                             btn_call.png |  +  |  +  |  +  |  +  |
     btn_check_off_focused_holo_light.png |  +  |  -  |  +  |  -  |
