'use strict';

angular.module('myApp.journal', ['ngRoute'])

    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/journal', {
            templateUrl: 'journal/journal.html',
            controller: 'journalCtrl'
        });
    }])


    .controller('journalCtrl', ["Restangular", "$scope", function (Restangular, $scope) {
        Restangular.all('journal-entries').getList().then(function (journalEntries) {
            $scope.journalEntries = journalEntries;

        });

         $scope.addEntry = function (journalEntry) {
            Restangular.one('journal-entries/').customPOST(journalEntry).then(function(journalEntry){
                 $scope.journalEntries.push(journalEntry)
                 $scope.journalEntry={};
            })

         };
    }]);