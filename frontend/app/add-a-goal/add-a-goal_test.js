'use strict';

describe('myApp.add-a-goal module', function() {

  beforeEach(module('myApp.add-a-goal'));

  describe('add-a-goal controller', function(){

    it('should ....', inject(function($rootScope, $controller) {
      //spec body
      var scope = $rootScope.$new();
      var AddAGoalCtrl = $controller('AddAGoalCtrl', {$scope: scope});
      expect(AddAGoalCtrl).toBeDefined();
    }));

  });
});