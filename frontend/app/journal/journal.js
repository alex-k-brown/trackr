'use strict';

angular.module('myApp.journal', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/journal', {
    templateUrl: 'journal/journal.html',
    controller: 'journalCtrl'
  });
}])

.controller('journalCtrl', [function() {

}]);