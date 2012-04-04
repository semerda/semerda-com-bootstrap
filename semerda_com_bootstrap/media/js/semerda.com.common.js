/*
 * Page methods
 * v0.1
 * By Ernest Semerda
 * Semerda.com
 *
 */

SEMERDA.page = (function () {

  return {
    // Update navigation with current position
    init : function(obj) {
        // Top navigation
        if (obj.primary >= 0) {
          $('#primary_nav li:eq(' + obj.primary + ')').addClass('active');
        }
        // Sidebar navigation
        if (obj.secondary >= 0) {
          $('#sidebar_nav li:eq(' + obj.secondary + ')').addClass('active');
        }
    }
  }
  
}());