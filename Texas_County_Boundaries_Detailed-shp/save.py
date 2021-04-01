
# coding: utf-8

# In[ ]:


<script>
$(function(){
        $.getJSON("mps.json", function(mps) {
            $("#output2").pivotUI(mps, {
                onRefresh: function(config) {
                    var config_copy = JSON.parse(JSON.stringify(config));
                    //delete some values which are functions
                    delete config_copy["aggregators"];
                    delete config_copy["renderers"];
                    //delete some bulky default values
                    delete config_copy["rendererOptions"];
                    delete config_copy["localeStrings"];
                    $("#output").text(JSON.stringify(config_copy, undefined, 2));
                }
            });
        });
     });
</script>

